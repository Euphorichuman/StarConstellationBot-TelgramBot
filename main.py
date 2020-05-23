from config import TOKEN
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
#from telegram import 
from bot import start
# @startconstellationbot

def main():
    #Se conecta con el bot
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("Start", start))

    #Ejecuta el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
