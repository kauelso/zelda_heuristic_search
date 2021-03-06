import numpy as np
import os

dir = os.path.dirname(__file__)
mapsDir = os.path.join(dir, './mapas/')

#Ler arquivo do mapa de hyrule
def getMapaHyrule():
    f = open(mapsDir + "hyrule.txt","r")
    data = np.array(f.read().split())
    f.close()
    return np.reshape(data,(42,42))

#Ler arquivo das dungeons
def getDungeons():
    f1 = open(mapsDir + "dungeon1.txt","r")
    data1 = np.array(f1.read().split())
    f1.close()

    f2 = open(mapsDir + "dungeon2.txt","r")
    data2 = np.array(f2.read().split())
    f2.close()

    f3= open(mapsDir + "dungeon3.txt","r")
    data3 = np.array(f3.read().split())
    f3.close()
    
    return (np.reshape(data1,(28,28)),np.reshape(data2,(28,28)),np.reshape(data3,(28,28)))