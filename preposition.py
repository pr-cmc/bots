import telebot
bot = telebot.TeleBot('')  #Сюда токен
admin = ['']  #Сюда ваш id
@bot.message_handler(commands=['start'])
def start(message):
  msg = bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, я бот для отправки предложки, напиши своё сообщение сюда и мы рассмотрим его в кратчайшие сроки')
  bot.register_next_step_handler(msg, request)
def request(message):
  bot.send_message(message.chat.id, '✅Ваше сообщение отправленно, ожидайте✅')
  for i in admin:
    bot.send_message(i, f"Новое предложение от Nekto:\n{message.text}")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)