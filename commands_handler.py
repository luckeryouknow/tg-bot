import telebot
import requests
from markups.charts_markup import charts_markup
from markups.currency_markup import currency_markup
from markups.price_changes_markup import price_changes_markup

API_TOKEN = '6388083417:AAFnoBZpLQkrrF95Bj9uq0nYma5EUt9qs1k'
bot = telebot.TeleBot(API_TOKEN)

CURRENCY_API_LINK = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10&currency=USD'

def reset_skip_currency():
    global skip_currency
    skip_currency = 0

def reset_skip_price():
    global skip_price
    skip_price = 0

def commands_handler(message):
    if message.chat.type == 'private':
        if message.text == 'Currency':
            response = requests.get(CURRENCY_API_LINK).json()['coins']
            response_message = ''

            for i in range(10):
                response_message += response[i]['name'] + ' - ' + str(round(response[i]['price'], 3)) + '$ \n'
                
            bot.send_message(message.chat.id, response_message, reply_markup=currency_markup)

            reset_skip_currency()

        elif message.text == 'Price changes':
            response = requests.get(CURRENCY_API_LINK).json()['coins']
            response_message = ''

            for i in range(10):
                response_message += response[i]['name'] + ": " + str(response[i]['priceChange1w']) + '% \n'
                
            bot.send_message(message.chat.id, response_message, reply_markup=price_changes_markup)
        
            reset_skip_price()

        elif message.text == 'Charts':
            bot.send_message(message.chat.id, "Choose the crypto-chart you need:", reply_markup=charts_markup)
