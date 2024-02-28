import telebot
from telebot import types
import os
bot = telebot.TeleBot('')#Сюда токен
@bot.message_handler(commands=['start'])
def start(message):
    openf = open("history.txt", 'a', encoding='utf-8')
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('📓Лента историй📓', callback_data='history_list')
    item2 = types.InlineKeyboardButton('➕Добавить историю➕', callback_data='add_history')
    item3 = types.InlineKeyboardButton('😌О боте😌', callback_data='about')
    markup.add(item, item2, item3)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def markup(call):
    if call.message:
        if call.data == 'about':
            bot.send_message(call.message.chat.id, 'Разработчик: @pr_cmc\nОписание: Я бот с историями. Здесь ты можешь читать и писать истории.')
        if call.data == 'add_history':
            bot.send_message(call.message.chat.id, 'Добавьте имя вашей истории и историю')
        if call.data == 'history_list':
            with open('history.txt', 'r', encoding='utf-8') as list:
                len = os.path.getsize("history.txt")
                if len > 0:
                    readl = list.read()
                    bot.send_message(call.message.chat.id, readl)
                else:
                    bot.send_message(call.message.chat.id, '🥺Увы, но историй пока нет🥺')
@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == message.text:
        with open('history.txt', 'a', encoding='utf-8') as list2:
            list2.write('\n' + message.text + '\n' + '________________'  + '\n')
    bot.send_message(message.chat.id, '✅История успешно добавлена✅')
    start(message)
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)