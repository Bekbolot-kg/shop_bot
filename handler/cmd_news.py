from aiogram import types
from parser.news import news_list

async def cmd_news(message: types.Message):
    for i in range(len(news_list)):
        await message.answer(news_list[i])