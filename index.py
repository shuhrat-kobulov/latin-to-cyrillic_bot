import telebot

from translate import to_cyrillic, to_latin
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None);

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, "Hello! Welcome to @Latin2Cyrilic_Bot")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  msg = message.text

  if msg.isascii():
    response = to_cyrillic(msg)
  else:
    response = to_latin(msg)

  bot.reply_to(message, response)

bot.polling()
