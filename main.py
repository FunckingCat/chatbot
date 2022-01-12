from typing import Text
import telebot
from telebot import apihelper
from telebot import types
from generator import get_name

TOKEN = '5001939735:AAHRF8K892p358JgH5cwApzWh2obwxnG-44'
bot = telebot.TeleBot(TOKEN)

sex = 10
format = 0
ammount = 1

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Мужской')
	itembtn2 = types.KeyboardButton('Женский')
	itembtn3 = types.KeyboardButton('Оба')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, "Выберите пол:", reply_markup=markup)

# @bot.message_handler(func=lambda m: m.text == "Мужской" or m.text == "Женский" or m.text == "Оба")
# def echo_all(message):
# 	if message.text == "Мужской":
# 		bot.send_message(message.chat.id, get_name(0))
# 	elif message.text == "Женский":
# 		bot.send_message(message.chat.id, get_name(1))
# 	elif message.text == "Оба":
# 		bot.send_message(message.chat.id, get_name())

@bot.message_handler(func=lambda m: m.text == "Мужской" or m.text == "Женский" or m.text == "Оба")
def echo_all(message):
	global sex
	if message.text == "Мужской":
		sex = 0
	elif message.text == "Женский":
		sex = 1
	elif message.text == "Оба":
		sex = 10
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Полное ФИО')
	itembtn2 = types.KeyboardButton('Фиамилия и инициалы')
	itembtn3 = types.KeyboardButton('Имя')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, "Выберите формат:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Полное ФИО" or m.text == "Фиамилия и инициалы" or m.text == "Имя")
def echo_all(message):
	global format
	if message.text == "Полное ФИО":
		format = 0
	elif message.text == "Фиамилия и инициалы":
		format = 1
	elif message.text == "Имя":
		format = 10
	markup = types.ReplyKeyboardMarkup(row_width=3)
	itembtn1 = types.KeyboardButton('1')
	itembtn2 = types.KeyboardButton('5')
	itembtn3 = types.KeyboardButton('10')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, "Выберите колличество:", reply_markup=markup)

@bot.message_handler(func=lambda m: int(m.text) > 0)
def echo_all(message):
	global ammount
	ammount = int(message.text)
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Мужской')
	itembtn2 = types.KeyboardButton('Женский')
	itembtn3 = types.KeyboardButton('Оба')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, make_answer(sex, format, ammount), reply_markup=markup)

def make_answer(sex, format, ammount):
	res = ""
	names = get_name(sex, ammount)
	for name in names:
		if format == 1:
			splitname = name.split()
			name = '{} {}. {}.'.format(splitname[0], splitname[1][0], splitname[2][0])
		elif format == 10:
			name = name.split()[1]
		res += name + '\n'
	return res

bot.infinity_polling()