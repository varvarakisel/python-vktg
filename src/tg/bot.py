import random
from telegram.ext import *
import settings 


print("working")

def start_command(update, context):
    update.message.reply_text("Привет, иди нахуй. Я бот, репостящий из вк в телегу, есть вопросы? Сука?")

def help_command(update, context):
    update.message.reply_text("Напиши ... чтобы ....")

def handle_message(update, context):
    text = str(update.message.text).lower()
    update.message.reply_text(text)

def error(update, context):
    print("ошибочка вышла")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
