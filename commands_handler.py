import telebot
import requests
from telebot import types

API_TOKEN = '6388083417:AAFnoBZpLQkrrF95Bj9uq0nYma5EUt9qs1k'
bot = telebot.TeleBot(API_TOKEN)

CURRENCY_API_LINK = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10&currency=USD'
CHARTS_API_LINK = 'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:ETHUSDT&width=600&height=400&interval=3M&theme=light'

currency_markup = types.InlineKeyboardMarkup()
currency_markup.row_width = 2
currency_markup.add(types.InlineKeyboardButton("<", callback_data="previous_currency"),
types.InlineKeyboardButton(">", callback_data="next_currency"))

price_changes_markup = types.InlineKeyboardMarkup()
price_changes_markup.row_width = 2
price_changes_markup.add(types.InlineKeyboardButton("<", callback_data="previous_price_changes"),
types.InlineKeyboardButton(">", callback_data="next_price_changes"))

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
            response = requests.get(CHARTS_API_LINK)
            
            bot.send_photo(message.chat.id, response.content)
            bot.send_message(message.chat.id, "Here's your chart")