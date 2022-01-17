from typing import Text
import telebot
from telebot import apihelper
from telebot import types
from const import *

#Ссылка на тест бота @test9182736419283764123_bot
#TOKEN = '5001939735:AAHRF8K892p358JgH5cwApzWh2obwxnG-44' # Рабочий API
TOKEN = '5047514937:AAEb3RBO2tkYRqMa7wbE6SwuDv3T2sZAogY' #Тест API
bot = telebot.TeleBot(TOKEN)

#Вот этот словарь передается в генератор
human = {
	'gender'   : '',
	'race'     : '',
	'class'    : '',
	'outlook'  : '',
	'kindness' : '',
}

def	make_markup(ch_dict): #Cоздает раскладку клавиатуры по словарю
	if (len(ch_dict) <= 5):
		markup = types.ReplyKeyboardMarkup(row_width=1)
	else:
		markup = types.ReplyKeyboardMarkup(row_width=2)
	btns = []
	for key in ch_dict:
		btn = types.KeyboardButton(ch_dict[key])
		btns.append(btn)
	i = 0
	while i < len(btns):
		if (i < len(btns) - 1):
			markup.add(btns[i], btns[i + 1])
		else:
			markup.add(btns[i])
		i += 2
	return markup

def	val_in_dict(string, ch_dict):
	for key in ch_dict:
		if ch_dict[key] == string:
			return True
	return False

def dict_to_string(d):
	st = ''
	for key in d:
		st += d[key] + ' '
	return st


@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = make_markup(genders)
	photo = open( welcome_image, 'rb')
	bot.send_photo(message.chat.id, photo)
	bot.send_message(message.chat.id, msg_gender, reply_markup=markup)

@bot.message_handler(func=lambda m: val_in_dict(m.text, genders))
def gernder_handler(message):
	global human
	human['gender'] = message.text
	markup = make_markup(races)
	bot.send_message(message.chat.id, msg_race, reply_markup=markup)

@bot.message_handler(func=lambda m: val_in_dict(m.text, races))
def race_handler(message):
	global human
	human['race'] = message.text
	markup = make_markup(classes)
	bot.send_message(message.chat.id, msg_class, reply_markup=markup)

@bot.message_handler(func=lambda m: val_in_dict(m.text, classes))
def calss_handler(message):
	global human
	human['class'] = message.text
	markup = make_markup(outlook_man)
	bot.send_message(message.chat.id, msg_outlook, reply_markup=markup)

@bot.message_handler(func=lambda m: val_in_dict(m.text, outlook_man))
def outlook_handler(message):
	global human
	human['outlook'] = message.text
	markup = make_markup(kindness_man)
	bot.send_message(message.chat.id, msg_kindness, reply_markup=markup)

@bot.message_handler(func=lambda m: val_in_dict(m.text, kindness_man))
def kindness_handler(message):
	global human
	human['kindness'] = message.text
	markup = make_markup(cmd)
	bot.send_message(message.chat.id, dict_to_string(human), reply_markup=markup)

@bot.message_handler()
def default_handler(message):
	markup = make_markup(cmd)
	bot.send_message(message.chat.id, msg_default, reply_markup=markup)

bot.infinity_polling()