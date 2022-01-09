import telebot
from telebot import apihelper

apihelper.ENABLE_MIDDLEWARE = True

TOKEN = '828038691:AAHdBswhWnKxBdQbBUy-uT-yXf4sEoD-GH0'
bot = telebot.TeleBot(TOKEN)

# @bot.middleware_handler(update_types=['message'])
# def modify_message(bot_instance, message):
#     message.text = message.text + ':changed'

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуй, {0.first_name}\n".format(message.from_user),parse_mode='html')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# repl = ""
	# for key in message:
	# 	repl += key + ' : ' + message[key] + '\n'
	bot.reply_to(message, message.chat)

@bot.message_handler(content_types= ["photo"])
def verifyUser(message):
	print ("Got photo")
	file_info = bot.get_file(message.photo[-1].file_id)
	file = bot.download_file(file_info.file_path)

	with open("image.jpg", 'wb') as new_file:
		new_file.write(file)

	bot.send_photo(message.chat.id, open("image.jpg", 'rb'))

# @bot.edited_message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()