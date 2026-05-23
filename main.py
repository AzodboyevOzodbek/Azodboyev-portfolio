import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

TEXT = """🏆Yutuqlar : Yoq

ɪɴꜱᴛᴀɢʀᴀᴍ : Azodboyev.o
ᴛᴇʟᴇɢʀᴀᴍ : @Azodboyev_o
ɢɪᴛʜᴜʙ : AzodboyevOzodbek"""

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, 'Salom! nima yordam bera olaman?')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Salom! Mening portfolio botimga xush kelibsiz!')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message.text + "\n\n" + TEXT)
	
bot.infinity_polling()