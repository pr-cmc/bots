import telebot
from telebot import types
import random
bot = telebot.TeleBot('6692773799:AAF6sNFIWiVKMCLdBBs3nZszCqGS03T0Rzk')
players = []
players2 = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_photo(message.chat.id, 'https://s.poembook.ru/theme/97/c2/0f/d7bcb057973c48bdd7e272c063f37355114770e0.jpeg', caption=f'Привет {message.from_user.first_name}!\nЯ бот для игры в русскую рулетку в группе или канале. Добавляй меня и играй. Удачи в игре!')
@bot.message_handler(commands=['newgame'])
def game(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item = types.KeyboardButton('1 патрон')
    item2 = types.KeyboardButton('Все патроны кроме одного')
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Выберите режим игры', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Все патроны кроме одного':
        players.clear()
        markup2 = types.ReplyKeyboardMarkup(row_width=1)
        item3 = types.KeyboardButton('Присоединиться')
        item4 = types.KeyboardButton('Играть')
        markup2.add(item3, item4)
        bot.send_message(message.chat.id, 'Нажмите присоединится (играют минимум 2 человека), после того как все присоединяться нажмите Играть!', reply_markup=markup2)
    if message.text == 'Присоединиться':
        msf = message.from_user.first_name
        if msf not in players:
            players.append(message.from_user.first_name)
    if message.text == 'Играть':
            if len(players) > 1:
            	bot.send_video(message.chat.id, 'https://i.gifer.com/embedded/download/JGSn.gif', caption=f'Курок взведен, узнаем кто умрет!', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
            	while len(players) != 1:
            	   i = random.choice(players)
            	   players.remove(i)
            	   bot.send_video(message.chat.id, 'https://avatars.dzeninfra.ru/get-zen_doc/1247665/pub_5ec492c4b6615326f01aa926_5ec493d0c9cc3601ef588157/orig', caption=f'{i} был(-а) застрелен(-а)')
            	if len(players) == 1:
            	     	bot.send_photo(message.chat.id, 'https://i.ytimg.com/vi/_oaSxfBUyhc/maxresdefault.jpg', caption=f'{players} остался(-ась) в живых! Игра окончена!')
    if message.text == '1 патрон':
        players2.clear()
        markup3 = types.ReplyKeyboardMarkup(row_width=1)
        item5 = types.KeyboardButton('Присоединиться к игре')
        item6 = types.KeyboardButton('Начать игру')
        markup3.add(item5, item6)
        bot.send_message(message.chat.id, 'Нажмите Присоединиться к игре (играют минимум 2 человека), после того как все присоединяться нажмите Начать игру!', reply_markup=markup3)
    if message.text == 'Присоединиться к игре':
        msf2 = message.from_user.first_name
        if msf2 not in players2:
            players2.append(message.from_user.first_name)
        if message.text == 'Начать игру':
            if len(players2) > 1:
                bot.send_video(message.chat.id, 'https://i.gifer.com/embedded/download/JGSn.gif', caption=f'Курок взведен, узнаем кто умрет!', reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')
                p = random.choice(players2)
                players2.remove(p)
                bot.send_video(message.chat.id, 'https://avatars.dzeninfra.ru/get-zen_doc/1247665/pub_5ec492c4b6615326f01aa926_5ec493d0c9cc3601ef588157/orig', caption=f'{p} был(-а) застрелен(-а)')
                bot.send_message(message.chat.id, f'{players2}, вы выжили! Игра окончена!')
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
