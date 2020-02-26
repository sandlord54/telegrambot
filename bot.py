import telebot
import requests
from bs4 import BeautifulSoup




TOKEN = '969612971:AAFxpDNtky1WBjuODbGbPja6j8vmDgHdNRo'
bot = telebot.TeleBot(TOKEN,threaded=False)


@bot.message_handler(content_types=['text'])
def send_mes (message):
    bot.send_message(message.chat.id, "Привет!\n"+res)
# RUN
bot.polling(none_stop=True)


