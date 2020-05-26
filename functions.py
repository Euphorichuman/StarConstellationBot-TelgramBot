import matplotlib.pyplot as plt
import random as rnd
import os
import os.path
from os import path

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
    return plt


#Función para graficar todas las estrellas y una constelación escogida por el usuario
def allStars1Constellation(name, figure, color):
    constellation = searchFile("./files/constellations/", name)

    #Realiza la búsqueda de cada par de estrellas
    starsFile = open("./files/stars.txt")
    starsWithNames = []
    cont = 0

    #Busca y almacena todas las estrellas que tengan nombre
    for line in starsFile:
        properties = line.split(" ")
        names = ""
        if (len(properties) >= 6):
            for i in range(6, len(properties)):
                if (properties[i][len(properties[i])-1] != ";"):
                    names = names + properties[i] + " "
                else:
                    names = names + properties[i]
            
            starsWithNames.append(names)
    
    #Busca cada par de estrellas
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for line in constellation:
        fields = line.split(",")
        starName1 = fields[0]
        starName2 = fields[1]
        index1 = 0
        index2 = 0
        for i in range(0, len(starsWithNames)):
            if (starsWithNames[i] != ""):
                aux = starsWithNames[i].split(";")
                for elem in aux:
                    if (starName1 == elem.strip()):
                        index1 = i+1

                    if (starName2.strip() == elem.strip()):
                        index2 = i+1
        starsFile.close()
        starsFile = open("./files/stars.txt")
        j = 0
        k = 0
        #print(index1)
        for line in starsFile:
            lineAux = line.split(" ")
            j = j + 1
            k = k + 1
            if (index1 == j):
                x1.append(lineAux[0])
                y1.append(lineAux[1])
            if (index2 == k):
                x2.append(lineAux[0])
                y2.append(lineAux[1])

    #figure.axis([-1,1,-1,1])
    for i in range(0, len(x1)):
        x = [float(x1[i]), float(x2[i])]
        y = [float(y1[i]), float(y2[i])]
        plt.plot(x,y, '.-', color = color)
    return plt

#Función para graficar todas las estrellas y todas las constelaciones
def starsAndContellations():
    plt = stars()
    listConstellations = os.listdir("./files/constellations")
    for each in listConstellations:
        name = each.split(".")[0]
        randomColor = [rnd.random(), rnd.random(), rnd.random()]
        allStars1Constellation(name, plt, randomColor)
    return plt


#Búsqueda de un archivo
def searchFile(dir, nameOfFile):
    name = nameOfFile + ".txt"
    content = os.listdir(dir)
    files = [nameContent for nameContent in content]
    found = ""
    for i in files:
        if (name == i):
            found = i
    dir = dir + found
    foundFile = open(dir, "r")
    return foundFile
