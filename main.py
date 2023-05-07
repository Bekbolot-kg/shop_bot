from aiogram import executor
from db.database import (init_db,
                         create_table,
                         insert_product,
                         delete_product,
                         get_product)
from handler.cmd_start import cmd_start
from handler.cmd_products import cmd_products, cb_products
from aiogram.dispatcher.filters import Text
from config import dp, scheduler
import logging

async def start_up(_):
    init_db()
    delete_product()
    create_table()
    insert_product()
    get_product()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_products, Text(equals='Список товаров 🔍'))
    dp.register_callback_query_handler(cb_products, lambda c: True)


    scheduler.start()
    executor.start_polling(dispatcher=dp, on_startup=start_up)