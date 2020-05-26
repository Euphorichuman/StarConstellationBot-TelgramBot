import telegram.ext
import messsages as msg
import functions as f
import matplotlib.pyplot as plt
import traceback 
import os
import os.path
from os import path

def start(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido {}, para conocer lo que puedo hacer utiliza el comando /Help.".format(nombre)
    update.message.reply_text(mensaje)

def help(update, context):
    update.message.reply_text(msg.helpMessage, parse_mode=telegram.ParseMode.HTML)

#Función para mandar la figura con todas las estrellas
def allStars(update, context):
    chat_id = update.message.chat.id
    figure = f.stars()
    figure.draw()
    figure.savefig("./files/stars.png")
    context.bot.send_photo(chat_id, open("./files/stars.png",'rb'))
    os.remove("./files/stars.png")

#Función para mandar la figura con todas las estrellas y una constelación
def allStars1Constellation(update, context):
    chat_id = update.message.chat.id
    messageUser = update.message.text
    constellation = messageUser.split(" ")

    try:
        f.searchFile("./files/constellations/", constellation[1])
        figure = f.allStars1Constellation(constellation[1], f.stars(), "#fdff6e")
        figure.savefig("./files/1Constellation.png")
        context.bot.send_photo(chat_id, open("./files/1Constellation.png",'rb'))
        os.remove("./files/1Constellation.png")
    except:
        update.message.reply_text(msg.errorMessage, parse_mode=telegram.ParseMode.HTML)

#Función para mandar la figura con todas las estrellas y todas las constelaciones
def allStarsAllConstellations(update, context):
    chat_id = update.message.chat.id
    figure = f.starsAndContellations()
    figure.draw()
    figure.savefig("./files/StarsAndConstellations.png")
    context.bot.send_photo(chat_id, open("./files/StarsAndConstellations.png",'rb'))
    os.remove("./files/StarsAndConstellations.png")


#Función para mandar una lista de las constelaciones disponibles
def constellations(update, context):
    update.message.reply_text(msg.constellationsMessage)

#Función para mandar una lista de las constelaciones disponibles
def about(update, context):
    update.message.reply_text(msg.infoMessage, parse_mode=telegram.ParseMode.HTML)

