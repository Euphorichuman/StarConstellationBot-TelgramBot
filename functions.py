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

