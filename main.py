import telebot
import requests
from telebot import types

API_TOKEN = '6388083417:AAFnoBZpLQkrrF95Bj9uq0nYma5EUt9qs1k'
CURRENCY_API_LINK = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10&currency=USD'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Currency')
    button2 = types.KeyboardButton('Price changes')
    button3 = types.KeyboardButton('Graphics')

    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Hi, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def commandsHandler(message):
    if message.chat.type == 'private':
        response = requests.get(CURRENCY_API_LINK).json()['coins']
        response_message = ''

        if message.text == 'Currency':
            for i in range(10):
                response_message += response[i]['name'] + ' - ' + str(response[i]['price']) + '$ \n'
            bot.send_message(message.chat.id, response_message)

        if message.text == 'Price changes':
            for i in range(10):
                response_message += response[i]['name'] + ": " + str(response[i]['priceChange1w']) + '% \n'
            bot.send_message(message.chat.id, response_message)
    

bot.infinity_polling()  