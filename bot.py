def start(update, context):
    nombre = update.message.chat.first_name
    mensaje = "Bienvenido {}, para conocer lo que puedo hacer utiliza el comando /Help.".format(nombre)
    update.message.reply_text(mensaje)

helpmessage = """Los astrónomos recopilan muchos datos sobre las estrellas, y hay muchos catálogos que identifican las ubicaciones de las mismas. 
Por lo anterior, al buscar información sobre las estas puede llegar a ser algo muy confuso, pero afortunamente estoy yo aquí para hacerte la vida más fácil.


Puedes controlarme enviando los siguientes comandos:

/AllStars - Para Mostrar un gráfico de todas las estrellas.
/AllStars1Constellation - Para Mostrar un gráfico de todas las estrellas y, adicionalmente, una constelación en particular, escogida por usted.
/AllStarsAllConstellations - Para mostrar un gráfico de todas las estrellas y todas las constelaciones.


Adicionalmente, si quieres conocerme un poco mejor, puedes visitar mi código fuente en: 
https://github.com/fuentesDeveloper/Telegram_Bot_Stars.git"""

def help(update, context):
    update.message.reply_text(helpmessage)

def allStars(update, context):
    update.message.reply_text("Para Mostrar un gráfico de todas las estrellas.")

def allStars1Constellation(update, context):
    update.message.reply_text("Mostrar un gráfico con todas las estrellas y, adicionalmente, una constelaci ́on en particular, escogida por el usuario.")

def allStarsAllConstellations(update, context):
    update.message.reply_text("Mostrar un gráfico de todas las estrellas y todas las constelaciones.")
