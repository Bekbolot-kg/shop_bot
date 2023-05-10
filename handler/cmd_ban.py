from aiogram import types
from handler.words import words

async def ban_bad_word(message: types.Message):
    """ Баннить пользователей которые пишет запрещенные слова """

    member_type = (await message.chat.get_member(message.from_user.id)).status
    if message.chat.type != 'private':

        for word in words:
            if word in message.text.lower().strip():
                await message.reply(f'Пользователь {message.from_user.full_name} заблокирован.\n'
                                    f'Причина: использование запрещенных слов.')

                if member_type != 'creator':
                    await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                break