import random, telebot
from telebot import types
from time import sleep
bot = telebot.TeleBot("")#Токен
@bot.message_handler(commands=["start"])
def start(message):
	markup = types.InlineKeyboardMarkup(row_width=3)
	item = types.InlineKeyboardButton("✊", callback_data="stone")
	item2 = types.InlineKeyboardButton("✌️", callback_data="scissors")
	item3 = types.InlineKeyboardButton("✋", callback_data="paper")
	markup.add(item, item2, item3)
	bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nВыбери:\nКамень✊\nНожницы✌️\nБумагу✋", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def button(call):
	if call.message:
		if call.data == "stone":
			list = ["stone", "scissors", "paper"]
			r = random.choice(list)
			bot.send_message(call.message.chat.id, "Твой ход")
			sleep(1)
			bot.send_message(call.message.chat.id, "✊")
			if r == "stone":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✊")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ничья!")
			if r == "scissors":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✌️")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты выиграл!")
			if r == "paper":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✋")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты проиграл!")
		if call.data == "scissors":
			list2 = ["stone", "scissors", "paper"]
			r2 = random.choice(list2)
			bot.send_message(call.message.chat.id, "Твой ход")
			sleep(1)
			bot.send_message(call.message.chat.id, "✌️")
			if r2 == "scissors":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✌️")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ничья!")
			if r2 == "paper":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✋")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты выиграл!")
			if r2 == "stone":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✊")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты проиграл!")
		if call.data == "paper":
			list3 = ["stone", "scissors", "paper"]
			r3 = random.choice(list3)
			bot.send_message(call.message.chat.id, "Твой ход")
			sleep(1)
			bot.send_message(call.message.chat.id, "✋")
			if r3 == "paper":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✋")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ничья!")
			if r3 == "stone":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✊")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты выиграл!")
			if r3 == "scissors":
				bot.send_message(call.message.chat.id,"Ход бота")
				sleep(1)
				bot.send_message(call.message.chat.id,"✌️")
				sleep(1)
				bot.send_message(call.message.chat.id,"Ты проиграл!")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(e)