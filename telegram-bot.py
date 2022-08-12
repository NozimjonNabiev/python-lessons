# 27-dars: Krill-Lotin bot
# Sana: 13/08/2022
# Muallif: Nozimjon Nabiev

from transliterate import to_cyrillic, to_latin

import telebot

TOKEN = '5411351087:AAGrp5vUP4VQvBOSxlu9TE6vLf0vRgUUcrU'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu Aleykum!"
    answer += " Menga matn jo'nating va men uni lotindan krillga yoki krilldan lotinga o'girib beraman:"
    bot.reply_to(message, answer)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text 
    text = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, text(msg))
    
    
bot.infinity_polling()