from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from config import STARTED_MESSAGE, MESSAGE_CONTACT
from database import db
import utils.keyboards as keyboards

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    if not await db.user.user_register(message.from_user.id):
        await db.user.create_user(message.from_user.id)
    await message.answer(STARTED_MESSAGE, reply_markup=keyboards.keyboard_started())

@router.message(F.text == "Связаться с поддержкой")
async def get_contact_handler(message: Message):
    await message.answer(MESSAGE_CONTACT)

@router.callback_query(F.data == "canceled")
async def canceled_to_filling_handler(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    try:
      await callback.message.edit_text((
          f"Действие было отменено"
      ))
    except:
        await callback.message.answer((
            f"Действие было отменено"
        ))