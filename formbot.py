import telebot
from telebot import types

bot = telebot.TeleBot('')  #Сюда токен
admin = ['']  #Сюда id чата с ботом(получить можно введя команду /id)


@bot.message_handler(commands=['start'])
def start(message):
  markup = types.InlineKeyboardMarkup(row_width=1)
  item = types.InlineKeyboardButton('📞Отправить заявку📞', callback_data='send')
  markup.add(item)
  bot.send_message(
      message.chat.id,
      f'Привет {message.from_user.first_name}, я бот для отправки заявки!',
      reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def markup(call):
  if call.message:
    if call.data == 'send':
      msg = bot.send_message(call.message.chat.id,
                             'Пожалуйста отправьте мне заявку')
      bot.register_next_step_handler(msg, request)


def request(message):
  bot.send_message(message.chat.id, '✅Спасибо, заявка отправлена!✅')
  for i in admin:
    bot.send_message(
        i, f"У вас заявка от @{message.from_user.username}:\n{message.text}")


@bot.message_handler(commands=['id'])
def id(message):
  bot.send_message(
      message.chat.id,
      f'ID чата - {message.chat.id}\nО боте:\nРазработчик: @pr_cmc\nОписание: Я бот для отправки заявок!'
  )
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)