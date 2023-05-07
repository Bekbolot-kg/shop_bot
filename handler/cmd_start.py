from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def cmd_start(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Список товаров 🔍'))
    await message.answer(text='Добро пожаловать в наш магазин аксессуаров 😃! Я чат-бот, который поможет вам с выбором и покупкой самых лучших товаров 🛒. Давайте начнем!',
                         reply_markup=kb)
    await message.delete()