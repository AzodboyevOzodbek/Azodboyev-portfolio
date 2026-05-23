import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

TEXT = """
ɪɴꜱᴛᴀɢʀᴀᴍ : Azodboyev.o
ᴛᴇʟᴇɢʀᴀᴍ : @Azodboyev_o
ɢɪᴛʜᴜʙ : AzodboyevOzodbek
"""

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, 'Salom! nima yordam bera olaman?')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Men haqimda')
    btn2 = types.KeyboardButton('Loyhalarim')
    btn3 = types.KeyboardButton('Boglanish')
    keyboard.add(btn1, btn2, btn3)
    text = 'Salom! Mening portfolio botimga xush kelibsiz!'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def replaybutton(message):
      text3 = """
👨‍💻 Azodboyev Ozodbek

📅 2012-yilda tug‘ilganman
🎮 O‘yinlar va dasturlashga qiziqaman
🤖 Telegram botlar va turli loyihalar ustida ishlayman
💡 Python va texnologiyalarni o‘rganishni yoqtiraman

🌐 Ijtimoiy tarmoqlar:
📸 Instagram: Azodboyev.o
💬 Telegram: @Azodboyev_o
🔗 GitHub: AzodboyevOzodbek
"""
      bot.send_message(message.chat.id, text3)
bot.infinity_polling()

