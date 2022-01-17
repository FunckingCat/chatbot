from typing import Text
import telebot
from telebot import apihelper
from telebot import types
from generator import generate_name
from const import *

#Ссылка на тест бота @test9182736419283764123_bot
#TOKEN = '5001939735:AAHRF8K892p358JgH5cwApzWh2obwxnG-44' # Рабочий API
TOKEN = '5047514937:AAEb3RBO2tkYRqMa7wbE6SwuDv3T2sZAogY' #Тест API
bot = telebot.TeleBot(TOKEN)

#Вот этот словарь передается в генератор


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

'''
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
'''


users = {}


class User:
	def __init__(self):
		self.human = {
			'gender'   : '',
			'race'     : '',
			'class'    : '',
			'outlook'  : '',
			'kindness' : '',
		}


def get_user(id):
	if id in users:
		return users[id].human
	users[id] = User()
	return users[id].human


@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = make_markup(genders)
	photo = open( welcome_image, 'rb')
	bot.send_photo(message.chat.id, photo)
	bot.send_message(message.chat.id, msg_gender, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in genders.values())
def gernder_handler(message):
	#global human
	get_user(message.from_user.id)['gender'] = message.text
	markup = make_markup(races)
	bot.send_message(message.chat.id, msg_race, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in races.values())
def race_handler(message):
	#global human
	get_user(message.from_user.id)['race'] = message.text
	markup = make_markup(classes)
	bot.send_message(message.chat.id, msg_class, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in classes.values())
def class_handler(message):
	#global human
	get_user(message.from_user.id)['class'] = message.text
	if get_user(message.from_user.id)['gender'] == 'Мужской':
		markup = make_markup(outlook_man)
	else:
		markup = make_markup(outlook_woman)
	bot.send_message(message.chat.id, msg_outlook, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in (list(outlook_man.values()) + list(outlook_woman.values())))
def outlook_handler(message):
	#global human
	get_user(message.from_user.id)['outlook'] = message.text
	if get_user(message.from_user.id)['gender'] == 'Мужской':
		markup = make_markup(kindness_man)
	else:
		markup = make_markup(kindness_woman)
	bot.send_message(message.chat.id, msg_kindness, reply_markup=markup)

@bot.message_handler(func=lambda m: m.text in (list(kindness_man.values()) + list(kindness_woman.values())))
def kindness_handler(message):
	#global human
	get_user(message.from_user.id)['kindness'] = message.text
	markup = make_markup(cmd)
	bot.send_message(message.chat.id, generate_name(get_user(message.from_user.id)), reply_markup=markup)

@bot.message_handler()
def default_handler(message):
	markup = make_markup(cmd)
	bot.send_message(message.chat.id, msg_default, reply_markup=markup)

bot.infinity_polling()
