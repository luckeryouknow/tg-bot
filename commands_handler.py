import telebot
import requests
from telebot import types

API_TOKEN = '6122625919:AAHRcg7YSpfzAIsABv0afJbp3GgmAwfQnQs'
bot = telebot.TeleBot(API_TOKEN)

CURRENCY_API_LINK = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10&currency=USD'
CHARTS_API_LINK = 'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:ETHUSD&width=600&height=400&interval=3M&theme=light'
ETH_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:ETHUSD&width=600&height=400&interval=3M&theme=light'
BTC_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:BTCUSD&width=600&height=400&interval=3M&theme=light'
USDT_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:USDTUSD&width=600&height=400&interval=3M&theme=light'
BNB_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:BNBUSD&width=600&height=400&interval=3M&theme=light'
XRP_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:XRPUSD&width=600&height=400&interval=3M&theme=light'
USDC_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:USDCUSD&width=600&height=400&interval=3M&theme=light'
LDO_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:LDOUSD&width=600&height=400&interval=3M&theme=light'
DOGE_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:DOGEUSD&width=600&height=400&interval=3M&theme=light'
ADA_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:ADAUSD&width=600&height=400&interval=3M&theme=light'
SOL_API_LINK = f'https://api.chart-img.com/v1/tradingview/mini-chart?key=qJX6lruQMB9Yhkj7ub87z3vrFa8z6hI13AgoaLdS&symbol=BINANCE:SOLUSD&width=600&height=400&interval=3M&theme=light'

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
charts_markup.add(types.InlineKeyboardButton("Choose another chart", callback_data="chart"))

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
                
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=charts_markup)

           
        elif message.text == 'Bitcoin':
            response = requests.get(BTC_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Ethereum':
            response = requests.get(ETH_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Tether':
            response = requests.get(USDT_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'BNB':
            response = requests.get(BNB_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'XRP':
            response = requests.get(XRP_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'USD Coin':
            response = requests.get(USDC_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Lido Stacked Ether':
            response = requests.get(LDO_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Dogecoin':
            response = requests.get(DOGE_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Cardano':
            response = requests.get(ADA_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)

        elif message.text == 'Solana':
            response = requests.get(SOL_API_LINK)
            bot.send_photo(message.chat.id, response.content)           
            bot.send_message(message.chat.id, "Here's your chart", reply_markup=markup)
