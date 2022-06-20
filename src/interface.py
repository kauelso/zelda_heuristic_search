import pygame
from math import floor

#Cores
COR_GRAMA = pygame.Color(146,208,80)
COR_AREIA = pygame.Color(196,188,150)
COR_FLORESTA = pygame.Color(0,176,80)
COR_MONTANHA = pygame.Color(148,138,84)
COR_AGUA = pygame.Color(84,141,212)
COR_CHAO_DUNGEON = pygame.Color(225, 225, 225)
COR_PAREDE_DUNGEON = pygame.Color(97, 97, 97)

#Construir mapa de hyrule
def buildMapa(display,data):
    offset = 20
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

#Construir uma dungeon
def buildDungeon(display,data):
    offset = 40
    for y in range(0,840,offset):
        for x in range(0,840,offset):
            
            dataX = floor(x/offset)
            dataY = floor(y/offset)

            if data[dataY][dataX] == 'F':
                pygame.draw.rect(display,COR_CHAO_DUNGEON,(x, y, offset, offset))
            else:
                pygame.draw.rect(display,COR_PAREDE_DUNGEON,(x, y, offset, offset))

            pygame.draw.rect(display, (0,0,0), (x,y,155,155), 1) #Borda
