from math import floor
import pygame, sys
from pygame.locals import *
import numpy as np

#Cores
COR_GRAMA = pygame.Color(146,208,80)
COR_AREIA = pygame.Color(196,188,150)
COR_FLORESTA = pygame.Color(0,176,80)
COR_MONTANHA = pygame.Color(148,138,84)
COR_AGUA = pygame.Color(84,141,212)
COR_CHAO_DUNGEON = pygame.Color(225, 225, 225)
COR_PAREDE_DUNGEON = pygame.Color(97, 97, 97)

#Construir mapa
def buildMapa(display,data,offset):
    for y in range(0,840,offset):
        for x in range(0,840,offset):
            
            dataX = floor(x/offset)
            dataY = floor(y/offset)

            if data[dataY][dataX] == 'G':
                pygame.draw.rect(display,COR_GRAMA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'S':
                pygame.draw.rect(display,COR_AREIA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'F':
                pygame.draw.rect(display,COR_FLORESTA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'M':
                pygame.draw.rect(display,COR_MONTANHA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'W':
                pygame.draw.rect(display,COR_AGUA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'D':
                pygame.draw.rect(display,COR_CHAO_DUNGEON,(x, y, offset, offset))
            else:
                pygame.draw.rect(display,COR_PAREDE_DUNGEON,(x, y, offset, offset))

            pygame.draw.rect(display, (0,0,0), (x,y,155,155), 1) #Borda

#Ler arquivo do mapa de hyrule
def getMapaHyrule():
    f = open("src\mapas\hyrule.txt","r")
    data = np.array(f.read().split())
    f.close()
    return np.reshape(data,(42,42))

def main():
    mapa = getMapaHyrule()
    pygame.init()

    DISPLAY = pygame.display.set_mode((840,840))
    pygame.display.set_caption('Legend of Zelda: A AI to the past')
    buildMapa(DISPLAY,mapa,20)

    while True: #Game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
            pygame.display.update()


if __name__ == '__main__':
    import sys
    sys.exit(main())