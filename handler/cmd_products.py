from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from remind.remind_every_day import start_remind
from db.database import get_product
import aiofiles


ikb1 = InlineKeyboardMarkup(row_width=2)
ikb1.add(InlineKeyboardButton(text='Наушники', callback_data='наушники'),
        InlineKeyboardButton(text='Мини принтеры', callback_data='мини_принтеры'),
        InlineKeyboardButton(text='Power Bank', callback_data='power_bank'),
        InlineKeyboardButton(text='Smart часы', callback_data='smart_часы'),
        InlineKeyboardButton(text='Получать уведомления о скидках', callback_data='скидка'))

async def cmd_products(message: types.Message):
    '''Для вывода список товаров и прикрепляет к ним кнопки в Inline режиме'''

    await message.answer(text='Список товаров 🔍', reply_markup=ikb1)
    await message.delete()

async def cb_products(callback: types.CallbackQuery):
    ''' Для обработки Inline кнопки и отправляет соответствующие товары '''

    ikb2 = InlineKeyboardMarkup(row_width=1)
    ikb2.add(InlineKeyboardButton(text='Купить', url='https://t.me/Bko04'),
              InlineKeyboardButton(text='Список товаров 🔍', callback_data='Список товаров'))


    if callback.data == 'наушники':
        for pr in get_product():
             if pr[1] == 'Наушники':
                async with aiofiles.open(pr[4], 'rb') as product_pic:
                    await callback.message.answer_photo(photo=product_pic,
                                                        caption=f'Наушник 🎧: {pr[2]},   цена 💸: {pr[3]} ',
                                                        parse_mode='HTML',
                                                        reply_markup=ikb2)
    elif callback.data == 'мини_принтеры':
        for pr in get_product():
             if pr[1] == 'Принтеры':
                async with aiofiles.open(pr[4], 'rb') as product_pic:
                    await callback.message.answer_photo(photo=product_pic,
                                                        caption=f'Принтер 🖨️: {pr[2]},  цена 💸: {pr[3]} ',
                                                        reply_markup=ikb2)
    elif callback.data == 'power_bank':
        for pr in get_product():
             if pr[1] == 'Power Bank':
                async with aiofiles.open(pr[4], 'rb') as product_pic:
                    await callback.message.answer_photo(photo=product_pic,
                                                        caption=f'Power Bank 🔋: {pr[2]},  цена 💸: {pr[3]} ',
                                                        reply_markup=ikb2)
    elif callback.data == 'smart_часы':
        for pr in get_product():
             if pr[1] == 'Smart часы':
                async with aiofiles.open(pr[4], 'rb') as product_pic:
                    await callback.message.answer_photo(photo=product_pic,
                                                        caption=f'Smart часы ⌚: {pr[2]},  цена 💸: {pr[3]} ',
                                                        reply_markup=ikb2)

    elif callback.data == 'Список товаров':
        await callback.message.answer(text='Список товаров 🔍', reply_markup=ikb1)

    elif callback.data == 'скидка':
        user_id = callback.from_user.id
        await start_remind(user_id)
        await callback.answer(text='Вам будут отправляться скидки на товары')


