from email.mime import message

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
    btn3 = types.KeyboardButton("Bog'lanish")
    btn4 = types.KeyboardButton('Yutuqlarim')
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    text = 'Salom! Mening portfolio botimga xush kelibsiz!'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def replaybutton(message):
    text3 = """
🧑‍💻 Azodboyev Ozodbek

📅 2012-yilda tug‘ilganman
🎮 O‘yinlar va dasturlashga qiziqaman
🤖 Telegram botlar va turli loyihalar ustida ishlayman
💡 Python va texnologiyalarni o‘rganishni yoqtiraman
"""
    bot.send_message(
        message.chat.id,text3)

@bot.message_handler(func=lambda m: m.text == "Bog'lanish")
def replaybutton(message):
    text4 = """Bog'lanish"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📸 Instagram', url="https://www.instagram.com/Azodboyev.o")
    btn2 = types.KeyboardButton('💬 Telegram', url="https://t.me/Azodboyev_o")
    btn3 = types.KeyboardButton('🔗 GitHub', url="https://github.com/AzodboyevOzodbek")
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id,
        text4,)

@bot.message_handler(func=lambda m: m.text == "Loyhalarim")
def replaybutton(message):
      text5 = """📂 Loyihalarim

1️⃣ 🤖 Portfolio Bot
👤 Men haqimda ma'lumot beradi
🛠 Python, Telegram Bot API

2️⃣ 🔄 Kirill ↔ Lotin Bot
🔤 Matnlarni avtomatik o‘giradi
🛠 Python

3️⃣ 🎬 Kino Bot
🎥 Kino qidirish va yuborish
🛠 Aiogram

4️⃣ 🌐 Web App
📱 Telegram uchun mini web ilova
🛠 HTML, CSS, JavaScript"""
      bot.send_message(message.chat.id, text5)

@bot.message_handler(func=lambda m: m.text == "Yutuqlarim")
def replaybutton(message):
    text6 = """🏆 Yutuqlarim"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton('1️⃣ 🏆 Createx Lending', url="https://createx-lending.vercel.app")
    btn2 = types.InlineKeyboardButton('2️⃣ 🏆 Strimline-Lending', url="https://strimline-lending.vercel.app")
    btn3 = types.InlineKeyboardButton('3️⃣ 🏆 Food-Website', url="https://food-website-lemon.vercel.app/")
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,text6)

bot.infinity_polling()

