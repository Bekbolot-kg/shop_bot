from aiogram import types
from parser.cars import cars

async def cmd_cars(message: types.Message):
    for i in range(len(cars)):
        await message.answer(cars[i])