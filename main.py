import telebot
from telebot import apihelper
from telebot import types
from generator import get_name

TOKEN = '828038691:AAHdBswhWnKxBdQbBUy-uT-yXf4sEoD-GH0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Мужской')
	itembtn2 = types.KeyboardButton('Женский')
	itembtn3 = types.KeyboardButton('Оба')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, "Выберите пол:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "Мужской":
		bot.send_message(message.chat.id, get_name(0))
	elif message.text == "Женский":
		bot.send_message(message.chat.id, get_name(1))
	elif message.text == "Оба":
		bot.send_message(message.chat.id, get_name())

bot.infinity_polling()