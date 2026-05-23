import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, 'Salom! nima yordam bera olaman?')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Salom! Mening portfolio botimga xush kelibsiz!')

bot.infinity_polling()