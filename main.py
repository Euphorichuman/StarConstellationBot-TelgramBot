from config import TOKEN
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
#from telegram import 
from bot import start, help, allStars, allStars1Constellation, allStarsAllConstellations, constellations
# @startconstellationbot

def main():
    #Se conecta con el bot
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("Start", start))
    dispatcher.add_handler(CommandHandler("Help", help))
    dispatcher.add_handler(CommandHandler("AllStars", allStars))
    dispatcher.add_handler(CommandHandler("AllStars1Constellation", allStars1Constellation))
    dispatcher.add_handler(CommandHandler("AllStarsAllConstellations", allStarsAllConstellations))
    dispatcher.add_handler(CommandHandler("Contellations", constellations))


    #Ejecuta el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
