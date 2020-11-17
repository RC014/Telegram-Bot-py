from telegram import Update
from telegram.ext import Updater, CallbackContext
from telegram.ext import CommandHandler
import math

updater = Updater(token='TOKEN-ul tau aici', use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
                     
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Alege formula care vreai s-o calculezi.")
    
#Partea orincipala a codului

updater.start_polling()
