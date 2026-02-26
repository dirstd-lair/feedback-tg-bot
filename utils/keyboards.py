from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def keyboard_started():
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text="Сообщить об ошибке")],
        [KeyboardButton(text="Связаться с поддержкой")]
    ])

def keyboard_canceled():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Отменить заполнение", callback_data="canceled")]
    ])