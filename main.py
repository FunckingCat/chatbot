from typing import Text
import telebot
from telebot import apihelper
from telebot import types
from generator import generate_name
from const import *

#Ссылка на тест бота @test9182736419283764123_bot
TOKEN = '5001939735:AAHRF8K892p358JgH5cwApzWh2obwxnG-44' # Рабочий API
#TOKEN = '5047514937:AAEb3RBO2tkYRqMa7wbE6SwuDv3T2sZAogY' #Тест API
bot = telebot.TeleBot(TOKEN)

#Вот этот словарь передается в генератор


def make_markup(ch_dict): #Cоздает раскладку клавиатуры по словарю
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

users = {}

class User:
    def __init__(self):
        self.state = 'PRE_MENU'
        self.data = {
            'name'     : '',
            'gender'   : 'Мужской',
            'race'     : '',
            'class'    : '',
            'outlook'  : '',
        }


def get_user(msg):
    uid = msg.from_user.id
    if uid in users:
        return users[uid]
    users[uid] = User()
    return users[uid]


@bot.message_handler(commands=['start'])
def start_command(msg):
    get_user(msg).state = 'PRE_MENU'
    pre_menu_state(msg)


@bot.message_handler(func=lambda msg: get_user(msg).state == 'PRE_MENU')
def pre_menu_state(msg):
    markup = make_markup(is_rand)
    #markup = make_markup(genders)
    photo = open( welcome_image, 'rb')
    bot.send_photo(msg.chat.id, photo)
    bot.send_message(msg.chat.id, 'Выберите: сгенерировать новое имя или именить ваше имя', reply_markup=markup)
    get_user(msg).state = 'MENU'


@bot.message_handler(func=lambda msg: get_user(msg).state == 'MENU')
def menu_state(msg):
    if msg.text == 'Изменить':
        get_user(msg).state = 'ENTER_NAME'
        markup = make_markup({'Назад': 'Назад'})
        bot.send_message(msg.chat.id, 'Введите своё имя', reply_markup=markup)
    elif msg.text == 'Случайное':
        get_user(msg).data['name'] = '__RANDOM__'
        get_user(msg).state = 'SELECT_RACE'
        select_race_state(msg)

@bot.message_handler(func=lambda msg: get_user(msg).state == 'ENTER_NAME')
def ender_name_state(msg):
    get_user(msg).data['name'] = msg.text
    get_user(msg).state = 'SELECT_RACE'
    select_race_state(msg)

@bot.message_handler(func=lambda msg: get_user(msg).state == 'SELECT_RACE')
def select_race_state(msg):
    if msg.text in races.values():
        get_user(msg).data['race'] = msg.text
        get_user(msg).state = 'SELECT_CLASS'
        select_class_state(msg)
    else:
        markup = make_markup(races)
        bot.send_message(msg.chat.id, 'Выберите расу:', reply_markup=markup)

@bot.message_handler(func=lambda msg: get_user(msg).state == 'SELECT_CLASS')
def select_class_state(msg):
    if msg.text in classes.values():
        get_user(msg).data['class'] = msg.text
        if get_user(msg).data['name'] == '__RANDOM__':
            get_user(msg).state = 'SELECT_SEX'
            select_sex_state(msg)
        else:
            get_user(msg).state = 'SELECT_OUTLOOK'
            select_outlook_state(msg)
    else:
        markup = make_markup(classes)
        bot.send_message(msg.chat.id, 'Выберите класс:', reply_markup=markup)

@bot.message_handler(func=lambda msg: get_user(msg).state == 'SELECT_SEX')
def select_sex_state(msg):
    if msg.text in genders.values():
        get_user(msg).data['gender'] = msg.text
        get_user(msg).state = 'SELECT_OUTLOOK'
        select_outlook_state(msg)
    else:
        markup = make_markup(genders)
        bot.send_message(msg.chat.id, 'Выберите пол:', reply_markup=markup)

@bot.message_handler(func=lambda msg: get_user(msg).state == 'SELECT_OUTLOOK')
def select_outlook_state(msg):
    if msg.text in outlooks.values():
        get_user(msg).data['outlook'] = msg.text
        get_user(msg).state = 'OUTPUT_NAME'
        output_name_state(msg)
    else:
        markup = make_markup(outlooks)
        bot.send_message(msg.chat.id, 'Выберите мировоззрение:', reply_markup=markup)


@bot.message_handler(func=lambda msg: get_user(msg).state == 'OUTPUT_NAME')
def output_name_state(msg):
    markup = make_markup(cmd)
    bot.send_message(msg.chat.id, generate_name(get_user(msg).data), reply_markup=markup)


@bot.message_handler()
def default_handler(msg):
    #markup = make_markup(cmd)
    get_user(msg).state = 'PRE_MENU'
    bot.send_message(msg.chat.id, 'Друг, ты что то перепутал')
    pre_menu_state(msg)

bot.infinity_polling()
