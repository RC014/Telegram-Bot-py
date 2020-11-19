from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot
from telegram.ext import Updater, CallbackContext, Filters, MessageHandler, CommandHandler
from telegram.utils.request import Request
import math
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

button_problem = "Problema"
option_1 = "Miscare rectilinie uniforma"
option_2 = "Miscare rectilinie neuniforma"

def button_problem_handler(update : Update, context : CallbackContext):
    text = update.message.text
    if text == option_1 or text == option_2:
        update.message.reply_text(text="OK")
    elif text != option_1:
        ReplyKeyboardRemove()
    reply_option = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = option_1)]], resize_keyboard=True)
    ReplyKeyboardRemove()

    update.message.reply_text(text= "Cu ce ai nevoie de ajutor?" , reply_markup = reply_option)


def message_handler(update : Update, context : CallbackContext):
    text = update.message.text
    if text == button_problem:
        return button_problem_handler(update = update, context = context)
    reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=button_problem)]], resize_keyboard = True)
    update.message.reply_text(text = """Salutare, sunt botul telegram ce te v-a ajuta cu fizica
Apasa butonul de mai jos""", reply_markup = reply_markup)


def sticker_handler(update: Update, context: CallbackContext):
    ReplyKeyboardRemove()

    update.message.reply_text(text=f"Sticker {type(MessageHandler)}")

def main():
    req = Request(connect_timeout = 0.5)
    bot = Bot(token='1415622035:AAF5KwXCTHRO1HahW7eg4xkXsuVlx1eOGn4', request = req)
    updater = Updater(bot = bot, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(filters = Filters.text, callback = message_handler))
    updater.dispatcher.add_handler(MessageHandler(filters = Filters.sticker, callback = sticker_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
