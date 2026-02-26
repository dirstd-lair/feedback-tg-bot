from aiogram import Router, F, exceptions
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config import FILLING_MESSAGE_1, FILLING_MESSAGE_2, SEND_MESSAGE_TO_ADMIN, ADMIN_ID_CHAT
from contextlib import suppress
from utils.logger import get_logger
from database import db

import utils.keyboards as keyboards
from utils import fsm

router = Router()
logger = get_logger(__name__)

@router.message(F.text == "Сообщить об ошибке")
async def start_filling_handler(message: Message, state: FSMContext):
    msg = await message.answer(FILLING_MESSAGE_1, reply_markup=keyboards.keyboard_canceled())
    await state.update_data(msg=msg)
    await state.set_state(fsm.AppFillingState.title)

@router.message(fsm.AppFillingState.title)
async def input_title_filling_handler(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    if not message.text:
      with suppress(exceptions.TelegramBadRequest):
        return await data.get("msg").edit_text((
            f"Пожалуйста, укажите свою причину обращения в текстовом виде.\n"
            f"Повторите попытку:"
        ), reply_markup=keyboards.keyboard_canceled())

    if len(message.text.strip()) > 255:
        with suppress(exceptions.TelegramBadRequest):
            return await data.get("msg").edit_text((
                f"Максимальная длинна причины обращения составляет 255 символов.\n"
                f"Введите заного вашу причину и постарайтесь указать её короче:\n\n"
                f"Ваша текущая причина:\n"
                f"<code>{message.text}</code>"
            ), reply_markup=keyboards.keyboard_canceled())

    await state.update_data(title=message.text)
    await data.get("msg").edit_text(FILLING_MESSAGE_2, reply_markup=keyboards.keyboard_canceled())
    await state.set_state(fsm.AppFillingState.description)

@router.message(fsm.AppFillingState.description)
async def input_description_filling_handler(message: Message, state: FSMContext):
    await message.delete()
    data = await state.get_data()
    if not message.text:
      with suppress(exceptions.TelegramBadRequest):
        return await data.get("msg").edit_text((
            f"Пожалуйста, укажите подробное описание в текстовом виде.\n"
            f"Повторите попытку:"
        ), reply_markup=keyboards.keyboard_canceled())

    app = await db.application.create_application(data.get("title", "Заголовок не найден"), message.text, message.from_user.id)
    if not app:
       logger.exception(f"Не удалось создать обращение в бд. Data: {app}")
       await data.get("msg").edit_text((
          f"Не удалось создать обращение, повторите попытку позже!"
       ))
       await state.clear()
       return

    await state.update_data(description=message.html_text)
    with suppress(exceptions.TelegramBadRequest):
      await data.get("msg").edit_text((
         f"Благодарим за обращение!\n"
         f"ID обращения: {app.id}"
      ))

    data = await state.get_data()
    title = data.get("title", "Заголовок не найден")
    description = data.get("description", "Описание не найдено")

    try:
       await message.bot.send_message(ADMIN_ID_CHAT, SEND_MESSAGE_TO_ADMIN.format(
          user_id=message.from_user.id,
          first_name=message.from_user.first_name,
          title=title,
          description=description
       ))
    except Exception as ex:
       logger.exception(f"Не удалось отправить сообщение в группу {ex}")
    finally:
       await state.clear()



