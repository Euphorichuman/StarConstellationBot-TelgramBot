import functions as f
import matplotlib.pyplot as plt 
import os
import os.path
from os import path

def start(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido {}, para conocer lo que puedo hacer utiliza el comando /Help.".format(nombre)
    update.message.reply_text(mensaje)

helpMessage = """Los astrónomos recopilan muchos datos sobre las estrellas, y hay muchos catálogos que identifican las ubicaciones de las mismas. 
Por lo anterior, al buscar información sobre las estas puede llegar a ser algo muy confuso, pero afortunamente estoy yo aquí para hacerte la vida más fácil.


Puedes controlarme enviando los siguientes comandos:

/AllStars - Para Mostrar un gráfico de todas las estrellas.
/AllStars1Constellation - Para Mostrar un gráfico de todas las estrellas y, adicionalmente, una constelación en particular, escogida por usted.
/AllStarsAllConstellations - Para mostrar un gráfico de todas las estrellas y todas las constelaciones.
/Constellations - Para mostrar la lista de constelaciones disponibles.


Adicionalmente, si quieres conocerme un poco mejor, puedes visitar mi código fuente en:
https://github.com/fuentesDeveloper/Telegram_Bot_Stars.git."""

def help(update, context):
    update.message.reply_text(helpMessage)

#Función para mandar la figura con todas las estrellas
def allStars(update, context):
    chat_id = update.message.chat.id
    figure = f.stars()
    plt.savefig("./files/stars.png")
    context.bot.send_photo(chat_id, open("./files/stars.png",'rb'))
    os.remove("./files/stars.png")

#Función para mandar la figura con todas las estrellas y una constelación
def allStars1Constellation(update, context):
    chat_id = update.message.chat.id
    messageUser = update.message.text
    userConstellation = messageUser + ".txt"
    if(path.exists(userConstellation)):
        figure = f.oneConstellation(messageUser)
        plt.savefig("./files/1Constellation.png")
        context.bot.send_photo(chat_id, open("./files/1Constellation.png",'rb'))
        os.remove("./files/1Constellation.png")
    else:
        mensaje = "Por favor, escoja una constelación válida. Si no conoce las constellaciones, utilice el comando /Constellations"
        update.message.reply_text(mensaje)

#Función para mandar la figura con todas las estrellas y todas las constelaciones
def allStarsAllConstellations(update, context):
    chat_id = update.message.chat.id
    figure = f.starsAndContellations()
    plt.savefig("./files/starsAndContellations.png")
    context.bot.send_photo(chat_id, open("./files/starsAndContellations.png",'rb'))
    os.remove("./files/starsAndContellations.png")

constellationsMessage = """Las constelaciones disponibles son:
-BOYERO
-CASIOPEA
-CAZO
-CYGNET
-GEMINIS
-HYDRA
-OSAMAYOR
-OSAMENOR"""

#Función para mandar una lista de las constelaciones disponibles
def constellations(update, context):
    update.message.reply_text(constellationsMessage)

