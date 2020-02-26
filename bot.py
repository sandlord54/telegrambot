import telebot
import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    global res
    soup = BeautifulSoup(html,"html.parser")
    h1 = soup.find('div', {'class':'weather__content_tab-temperature'})
    opisanie = soup.find('div', {'class':'weather__article_description-text'})
    temp = soup.find('div', {'class':'weather__article_main_temp'})
    res = opisanie.text +'\n'+ 'Температура в Рыбинске сейчас:'+temp.text+h1.text
    print(res)



def glob():
    html = get_html('https://sinoptik.com.ru/погода-рыбинск-100500004')
    get_data(html)

if __name__ == '__main__':
    glob()


TOKEN = '969612971:AAFxpDNtky1WBjuODbGbPja6j8vmDgHdNRo'
bot = telebot.TeleBot(TOKEN,threaded=False)


@bot.message_handler(content_types=['text'])
def send_mes (message):
    bot.send_message(message.chat.id, "Привет!\n"+res)
# RUN
bot.polling(none_stop=True)


