import telebot
from telebot import types
from inline_buttons_handler import handle_next_currency_button, handle_next_price_button, handle_previous_currency_button, handle_previous_price_button, handle_chart_button
from commands_handler import commands_handler

API_TOKEN = '6122625919:AAHRcg7YSpfzAIsABv0afJbp3GgmAwfQnQs'

bot = telebot.TeleBot(API_TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Currency')
button2 = types.KeyboardButton('Price changes')
button3 = types.KeyboardButton('Charts')

markup.add(button1, button2, button3)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, {0.first_name}'.format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types='text')
def commands_wrapper(message):
    commands_handler(message)
            
@bot.callback_query_handler(func=lambda call: call.data.startswith('previous_currency'))
def previous_currency_wrapper(call):
    handle_previous_currency_button(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith('next_currency'))
def next_currency_wrapper(call):
    handle_next_currency_button(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith('previous_price_changes'))
def previous_pice_wrapper(calc):
    handle_previous_price_button(calc)

@bot.callback_query_handler(func=lambda call: call.data.startswith('next_price_changes'))
def next_price_wrapper(calc):
    handle_next_price_button(calc)

@bot.callback_query_handler(func=lambda call: call.data.startswith('chart'))
def chart_wrapper(message):
    handle_chart_button(message)
    
bot.polling(none_stop=True)
