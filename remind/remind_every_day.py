from config import scheduler, bot
from db.database import get_product
from random import choice


async def start_remind(user_id: int):
    """ Добавляет задание в планировщик заданий на отправку напоминаний пользователю. """

    scheduler.add_job(
        send_remind,
        'interval',
        hours=36,
        args=(user_id,)
    )


async def send_remind(user_id: int):
    """ Отправляет уведомления пользователю. """

    try:

        list_pr = []
        for pr in get_product():
            if pr[1] == 'Наушники':
                list_pr.append(pr)

        len_pr = list(range(len(list_pr)))
        which_pr = choice(len_pr)

        with open(list_pr[which_pr][4], 'rb') as product_pic:
            await bot.send_photo(
                chat_id=user_id,
                photo=product_pic,
                caption=f'Наушник 🎧: {list_pr[which_pr][2]},   Цена 💸: {list_pr[which_pr][3]} ',
                parse_mode='HTML')

    except Exception as e:
        print(e)
