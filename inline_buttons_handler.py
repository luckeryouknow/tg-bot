import telebot
import requests
from telebot import types

API_TOKEN = '6122625919:AAHRcg7YSpfzAIsABv0afJbp3GgmAwfQnQs'
bot = telebot.TeleBot(API_TOKEN)

skip_currency = 0
skip_price = 0

currency_markup = types.InlineKeyboardMarkup()
currency_markup.row_width = 2
currency_markup.add(types.InlineKeyboardButton("<", callback_data="previous_currency"),
types.InlineKeyboardButton(">", callback_data="next_currency"))

price_changes_markup = types.InlineKeyboardMarkup()
price_changes_markup.row_width = 2
price_changes_markup.add(types.InlineKeyboardButton("<", callback_data="previous_price_changes"),
types.InlineKeyboardButton(">", callback_data="next_price_changes"))

charts_markup = types.InlineKeyboardMarkup()
charts_markup.row_width = 6
charts_markup.add(types.InlineKeyboardButton("Choose the other chart", callback_data="chart"))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
variant1 = types.KeyboardButton('Bitcoin')
variant2 = types.KeyboardButton('Ethereum')
variant3 = types.KeyboardButton('Tether')
variant4 = types.KeyboardButton('BNB')
variant5 = types.KeyboardButton('XRP')
variant6 = types.KeyboardButton('USD Coin')
variant7 = types.KeyboardButton('Lido Stacked Ether')
variant8 = types.KeyboardButton('Dogecoin')
variant9 = types.KeyboardButton('Cardano')
variant10 = types.KeyboardButton('Solana')

markup.add(variant1, variant2, variant3, variant4, variant5, variant6, variant7, variant8, variant9, variant10)

def handle_previous_currency_button(call):
    global skip_currency

    if skip_currency > 0:
        skip_currency -= 10 

    API_LINK = f'https://api.coinstats.app/public/v1/coins?skip={skip_currency}&limit=10&currency=USD'

    response = requests.get(API_LINK).json()['coins']
    response_message = ''

    for i in range(10):
        response_message += response[i]['name'] + ' - ' + str(round(response[i]['price'], 3)) + '$ \n'

    bot.send_message(call.message.chat.id, response_message, reply_markup=currency_markup)

def handle_next_currency_button(call):
    global skip_currency

    if skip_currency < 60:
        skip_currency += 10 

    API_LINK = f'https://api.coinstats.app/public/v1/coins?skip={skip_currency}&limit=10&currency=USD'

    response = requests.get(API_LINK).json()['coins']
    response_message = ''

    for i in range(10):
        response_message += response[i]['name'] + ' - ' + str(round(response[i]['price'], 3)) + '$ \n'

    bot.send_message(call.message.chat.id, response_message, reply_markup=currency_markup)

def handle_previous_price_button(call):
    global skip_price

    if skip_price > 0:
        skip_price -= 10 

    API_LINK = f'https://api.coinstats.app/public/v1/coins?skip={skip_price}&limit=10&currency=USD'

    response = requests.get(API_LINK).json()['coins']
    response_message = ''

    for i in range(10):
        response_message += response[i]['name'] + ": " + str(response[i]['priceChange1w']) + '% \n'

    bot.send_message(call.message.chat.id, response_message, reply_markup=price_changes_markup)

def handle_next_price_button(call):
    global skip_price

    if skip_price < 60:
        skip_price += 10 

    API_LINK = f'https://api.coinstats.app/public/v1/coins?skip={skip_price}&limit=10&currency=USD'

    response = requests.get(API_LINK).json()['coins']
    response_message = ''

    for i in range(10):
        response_message += response[i]['name'] + ": " + str(response[i]['priceChange1w']) + '% \n'

    bot.send_message(call.message.chat.id, response_message, reply_markup=price_changes_markup)

def handle_chart_button(call):
             
    bot.send_message(call.message.chat.id, "Choose your chart", reply_markup=markup)

    
