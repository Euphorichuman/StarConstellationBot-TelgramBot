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

def allStarsAllConstellations():
    starsfile = open("./files/stars.txt","r")
    cont = 0
    x = []
    y = []
    nameslist = []
    for line in starsfile:
    fields = line.split(" ")
    x.insert(cont, float(fields[0]))
    y.insert(cont, float(fields[1]))
    if len(fields) == 7:
        names = fields[6]
        names = names.split(";")
        names = [name.strip() for name in names]
        nameslist.insert(cont, names)
        cont += 1
    if len(fields) == 8:
        names = fields[6]+" "+fields[7]
        names = names.split(";")
        names = [name.strip() for name in names]
        nameslist.insert(cont, names)
        cont += 1 
    if len(fields) == 9:
        st = ""
        st = fields[6]
        end = len(st)
        names = st[0:end]+fields[7]+" "+fields[8]
        names = names.split(";")
        names = [name.strip() for name in names]
        nameslist.insert(cont, names)
        cont += 1
    if len(fields) == 10:
        st = ""
        st = fields[7]
        end = len(st)
        names = fields[6]+" "+st[0:end]+fields[8]+" "+fields[9]
        names = names.split(";")
        names = [name.strip() for name in names]
        nameslist.insert(cont, names)
        cont += 1 
    starsfile.close()

    BoyeroFile = open("./files/constellations/Boyero.txt","r")
    CasiopeaFile = open("./files/constellations/Casiopea.txt","r")
    CazoFile = open("./files/constellations/Cazo.txt","r")
    CygnetFile = open("./files/constellations/Cygnet.txt","r")
    GeminisFile = open("./files/constellations/Geminis.txt","r")
    HydraFile = open("./files/constellations/Hydra.txt","r")
    OsaMFile = open("./files/constellations/OsaMayor.txt","r")
    OsamFile = open("./files/constellations/OsaMenor.txt","r")
    XY = []
    cont = 0
    xy1 = ""
    xy2 = ""

    for line in HydraFile:
    field = line.split(",")
    for line2 in nameslist:
      if len(line2) == 1:
        if field[0] == line2[0]:
          xy1 = str(x[cont])+","+str(y[cont])
        if field[1].strip("\n") == line2[0]:
          xy2 = str(x[cont])+","+str(y[cont])

      elif len(line2) == 2:
        if field[0] == line2[0] or field[0] == line2[1]:
          xy1 = str(x[cont])+","+str(y[cont])
        if field[1].strip("\n") == line2[0] or field[1] == line2[1]:
          xy2 = str(x[cont])+","+str(y[cont])
    
    cont += 1
    XY.insert(cont, xy1+";"+xy2)

    scale = 1
    figureMap = plt.figure(figsize=(15, 15))
    axis = plt.subplot(facecolor=("#000000"))
    plt.scatter(x,y, scale, facecolor=("#feffd8"))
    xx = []
    yy = []
    cont = 0

    for Dots in XY:
        Dots = Dots.split(";")
        dots1 = Dots[0].split(",")
        dots2 = Dots[1].split(",")
        xx = [float(dots1[0]),float(dots2[0])]
        yy = [float(dots1[1]),float(dots2[1])]
        plt.plot(xx, yy, marker = '.')
    
    return[plt.draw()] 

