import telebot, traceback, threading
from time import sleep
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#___________Импорт библиотек_____________
token = ""#Токен
bot = telebot.TeleBot(token) #Токен
#___________Токен________________________
np = []
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    add = InlineKeyboardButton("+", callback_data="new")
    keyboard.add(add)
    bot.send_message(message.chat.id, "Для создания нового процесса нажмите на кнопку ,,+'', для ручного отключения процесса удалите пост из переписки с ботом", reply_markup=keyboard)
#___________Обрабатываем старт____________
@bot.callback_query_handler(func=lambda call: True)
def markup(call):
    if call.message:
        if call.data == "new":
            np.clear()
            bot.answer_callback_query(callback_query_id=call.id)
            msg = bot.send_message(call.message.chat.id, "Отправьте боту сообщение с данными, записанными в солбик в таком порядке:\nID Телеграмм канала\nВремя в секундах, через которое пост повторно отправится\nКоличество постов")
            bot.register_next_step_handler(msg, next)
def next(message):
    if str(message.text).count("\n") == 2:
        np.append(message.text)
        m = bot.send_message(message.chat.id, "Отправьте пост боту\n❗До завершения процесса не удаляйте пост из переписки с ботом❗")
        bot.register_next_step_handler(m, new_process)
    else: bot.send_message(message.chat.id, "Данные не верны")
def new_process(message):
    np.append(message.message_id)
    np.append(message.chat.id)
    thread = threading.Thread(target=post, args=(np[0], np[1], np[2]))
    thread.start()
    thread.join()
#___________Обрабатываем создание нового процесса__________
def post(form, post, chat):
    while True:
        try:
            for i in range(int(form.split("\n")[2])): #Выполняем цикл с количеством отправленных сообщений
                bot.copy_message(int(form.split("\n")[0]), chat, post) #Отправляем сообщение в чат
                sleep(int(form.split("\n")[1])) #Делаем временной промежуток
        except Exception as e:
            break
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as error:
        print(traceback.print_exc())
#___________Запуск бота___________________