import telebot

bot = telebot.TeleBot("")  #Сюда телеграм API
admin = ['']  #Сюда свой телеграм id


@bot.message_handler(commands=["start"])
def start(message):
  f = open('usr.txt', 'a')
  file = open('usr.txt', 'r')
  if str(message.chat.id) not in file.read():
    f.write(str(message.chat.id) + '\n')
    f.close()
  bot.send_message(
      message.chat.id,
      f"Здравствуйте, {message.from_user.first_name}!\nЯ бот для принятия рассылок!"
  )


@bot.message_handler(content_types=['text'])
def mes(message):
  if str(message.from_user.id) in admin:
    bot.send_message(message.chat.id, "✅Рассылка успешно запущена✅"),
    rass = open('usr.txt', 'r')
    data = rass.readlines()
    for i in data:
      bot.send_message(
          i, f'Здравствуйте, {message.from_user.first_name}!\n{message.text}')
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)