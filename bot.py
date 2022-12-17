from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import lorem

import config

updater = Updater(config.TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Lorem Ipsum Bot! Type /help for information!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Enter /generate to generate Lorem Ipsum text")

def generate(update: Update, context: CallbackContext):
    loremText = lorem.text()
    update.message.reply_text(loremText)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('generate', generate))

updater.start_polling()