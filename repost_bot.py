import telebot, sqlite3, traceback
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#___________Импорт библиотек_____________
db = sqlite3.connect("channels.db", check_same_thread=False) #Присоединяемся к бд
cur = db.cursor() #Создаем курсор бд
cur.execute('''
    Create table if not exists data(
            id integer primary key,
            channel_1 integer not null,
            channel_2 integer not null
        )
''')
#___________Конфигурация бд______________
token = ""#Токен
bot = telebot.TeleBot(token) #Токен
#___________Токен________________________
@bot.message_handler(commands=["start"])
def start(message):
    data = ""
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i in range(0, int(str(cur.execute("SELECT COUNT(*) FROM data").fetchone()).replace("(", "").replace(")", "").replace(",", ""))):
        data += f"{str(cur.execute("SELECT channel_1 FROM data").fetchall()[i]).replace("(", "").replace(")", "").replace(",", "")} → {str(cur.execute("SELECT channel_2 FROM data").fetchall()[i]).replace("(", "").replace(")", "").replace(",", "")}\n"
    b1 = InlineKeyboardButton("➕Добавить канал➕", callback_data="add")
    b2 = InlineKeyboardButton("❌Удалить канал❌", callback_data="remove")
    keyboard.add(b1, b2)
    bot.send_message(message.chat.id, f"Ваши каналы:\n{data}", reply_markup=keyboard)
#___________Обрабатываем старт____________
@bot.callback_query_handler(func=lambda call : True)
def buttons(call):
    if call.message:
        if call.data == "add":
            msg1 = bot.send_message(call.message.chat.id, "Отправьте боту ID 1-го и 2-го канала через пробел")
            bot.register_next_step_handler(msg1, add)
        if call.data == "remove":
            msg2 = bot.send_message(call.message.chat.id, "Отправьте боту ID 1-го канала")
            bot.register_next_step_handler(msg2, delete)
def delete(message):
    info = cur.execute('SELECT * FROM data WHERE channel_1=?', (message.text, ))
    if info.fetchone() != None:
        cur.execute("delete from data where channel_1 = ?", (message.text, ))
        db.commit()
        bot.send_message(message.chat.id, "✅Канал успешно удален✅")
    else:
        bot.send_message(message.chat.id, "❌Такой канал уже существует❌")
    start(message)
#___________Обрабатываем удаление_________
def add(message):
    if " " in message.text and len(str(message.text).split()) == 2:
        info2 = cur.execute('SELECT * FROM data WHERE channel_1=? and channel_2=?', (str(message.text).split()[0], str(message.text).split()[1]))
        if info2.fetchone() == None:
            cur.execute("INSERT INTO data(channel_1, channel_2) VALUES(?, ?)", (str(message.text).split()[0], str(message.text).split()[1]))
            db.commit()
            bot.send_message(message.chat.id, "✅Канал успешно добавлен✅")
        else:
            bot.send_message(message.chat.id, "❌Такой канал уже существует❌")
    start(message)
#___________Обрабатываем добавление________
@bot.channel_post_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact"])
def repost(message):
    if message.chat.type == "channel":
        info3 = cur.execute('SELECT * FROM data WHERE channel_1=?', (message.chat.id, ))
        if info3.fetchone() != None: bot.forward_message(int(cur.execute("select * from data where channel_1 = ?", (message.chat.id, )).fetchone()[2]), message.chat.id, message.message_id)
#___________Обрабатываем пересылку из одного телеграм канала в другой______
while True:
    try:
        bot.polling(none_stop=True) #Запускаем телеграмм бота
    except Exception as error:
        print(traceback.print_exc())
#___________Запуск бота___________________
