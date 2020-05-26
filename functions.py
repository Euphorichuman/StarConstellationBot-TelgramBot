import matplotlib.pyplot as plt

#Función para graficar todas las estrellas
def stars():
    starsfile = open("./files/stars.txt","r")
    cont = 0
    x = []
    y = []
    nameslist = []
    for line in starsfile:
        fields = line.split(" ")
        x.insert(cont, float(fields[0]))
        y.insert(cont, float(fields[1]))
        if len(fields) > 6:
            names = fields[6:]
            names = " ".join(names)
            names = names.split(";")
            names = [name.strip() for name in names]
            nameslist.insert(cont, names)
        else:
            nameslist.insert(cont, "")  
            cont += 1 
    starsfile.close()

    scale = 1
    figureMap = plt.figure(figsize=(15, 15))
    axis = plt.subplot(facecolor=("#000000"))
    plt.scatter(x,y, scale, facecolor=("#feffd8"))
    return[plt.draw()]

#Función para graficar todas las estrellas y una constelación escogida por el usuario
def oneConstellation(constellation):
    userFile = constellation + ".txt"
    starsfile = open("./files/stars.txt","r")
    cont = 0
    x = []
    y = []
    nameslist = []
    for line in starsfile:
        fields = line.split(" ")
        x.insert(cont, float(fields[0]))
        y.insert(cont, float(fields[1]))
        if len(fields) > 6:
            names = fields[6:]
            names = " ".join(names)
            names = names.split(";")
            names = [name.strip() for name in names]
            nameslist.insert(cont, names)
        else:
            nameslist.insert(cont, "")  
            cont += 1 
    starsfile.close()
    scale = 1
    figureMap = plt.figure(figsize=(15, 15))
    axis = plt.subplot(facecolor=("#000000"))
    plt.scatter(x,y, scale, facecolor=("#feffd8"))

    userfile = open(userFile, "r")
    for line in userfile:
        fields = line.split(",")
        star1 = fields[0].strip()
        start2 = fields[1].strip()
        cont = 0
        x1 = []
        y1 = []
        for name in nameslist:
            if star1 in name:
                x1.insert(0, x[cont])
                y1.insert(0, y[cont])
            if start2 in name:
                x1.insert(1, x[cont])
                y1.insert(1, y[cont])
        i = i+1
        plt.plot(x1, y1, 'y--')
        x1.clear()
        y1.clear() 
    userfile.close()  
    return[plt.draw()] 

#Función para graficar todas las estrellas y todas las constelaciones
def starsAndContellations():
    starsfile = open("./files/stars.txt","r")
    cont = 0
    x = []
    y = []
    nameslist = []
    for line in starsfile:
        fields = line.split(" ")
        x.insert(cont, float(fields[0]))
        y.insert(cont, float(fields[1]))
        if len(fields) > 6:
            names = fields[6:]
            names = " ".join(names)
            names = names.split(";")
            names = [name.strip() for name in names]
            nameslist.insert(cont, names)
        else:
            nameslist.insert(cont, "")  
            cont += 1 
    starsfile.close()
    scale = 1
    figureMap = plt.figure(figsize=(15, 15))
    axis = plt.subplot(facecolor=("#000000"))
    plt.scatter(x,y, scale, facecolor=("#feffd8"))

    constellations = ["BOYERO", "CASIOPEA", "CAZO", "CYGNET", "GEMINIS", "HYDRA", "OSAMAYOR", "OSAMENOR"]
    for constellation in constellations:
        constellationsfile = open(constellation +".txt", "r")
        for line in constellationsfile:
            fields = line.split(",")
            star1 = fields[0].strip()
            star2 = fields[1].strip()
            i = 0
            x1 = []
            y1 = []
            for name in nameslist:
                if star1 in name:
                    x1.insert(0, x[i])
                    y1.insert(0, y[i])
                if star2 in name:
                    x1.insert(1, x[i])
                    y1.insert(1, y[i])
            i = i+1
            plt.plot(x1, y1, 'y--')
            x1.clear()
            y1.clear() 
        constellationsfile.close()
    return[plt.draw()] 
