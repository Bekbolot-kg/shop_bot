# list_pr = []
#         for pr in get_product():
#             if pr[1] == 'Наушники':
#                 list_pr.append(pr)
#
#         len_pr = list(range(len(list_pr)))
#
#         with open(list_pr[choice(len_pr)], 'rb') as product_pic:
#             await bot.send_photo(
#                 chat_id=user_id,
#                 photo=product_pic,
#                 caption=f'Наушник 🎧: {pr[2]},   Цена 💸: {pr[3]} ',
#                 parse_mode='HTML'

# await bot.send_message(
#                 chat_id=user_id,
#                 text="Приветствуем! 🛍️  Хотим поделиться с вами хорошей новостью - наш товар теперь доступен по сниженной"
#                      " цене! 😃 Спешите приобрести его, пока действует акция. 💰")