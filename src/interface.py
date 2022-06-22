import pygame
from math import floor
import os

dir = os.path.dirname(__file__)
assetsDir = os.path.join(dir, '../assets/')

#Cores
COR_GRAMA = pygame.Color(146,208,80)
COR_AREIA = pygame.Color(196,188,150)
COR_FLORESTA = pygame.Color(0,176,80)
COR_MONTANHA = pygame.Color(148,138,84)
COR_AGUA = pygame.Color(84,141,212)
COR_CHAO_DUNGEON = pygame.Color(225, 225, 225)
COR_PAREDE_DUNGEON = pygame.Color(97, 97, 97)

#Assets
LINK = pygame.image.load(assetsDir + 'link.png')
PORTA = pygame.image.load(assetsDir + 'door.png')
CASA = pygame.image.load(assetsDir + 'door_house.png')
ESPADA = pygame.image.load(assetsDir + 'sword.png')


pingenteAzul = pygame.image.load(assetsDir + 'pingente_azul.webp')
pingenteAzul = pygame.transform.scale(pingenteAzul, (15, 15))

pingenteVermelho = pygame.image.load(assetsDir + 'pingente_vermelho.webp')
pingenteVermelho = pygame.transform.scale(pingenteVermelho, (15, 15))

pingenteVerde = pygame.image.load( assetsDir + 'pingente_verde.webp')
pingenteVerde = pygame.transform.scale(pingenteVerde, (15, 15))

def posicaoRelativaMapa(posicao):
    return ((posicao[0]*10),(posicao[1]*10))

def posicaoRelativaDungeon(posicao):
    return ((posicao[0]*15),(posicao[1]*15))

#Construir mapa de hyrule
def buildMapa(display,data):
    offset = 10
    for y in range(0,420,offset):
        for x in range(0,420,offset):
            
            dataX = floor(x/offset)
            dataY = floor(y/offset)

            if data[dataY][dataX] == 'G':
                pygame.draw.rect(display,COR_GRAMA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'A':
                pygame.draw.rect(display,COR_AREIA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'F':
                pygame.draw.rect(display,COR_FLORESTA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'M':
                pygame.draw.rect(display,COR_MONTANHA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'R':
                pygame.draw.rect(display,COR_AGUA,(x, y, offset, offset))
            elif data[dataY][dataX] == 'W':
                pygame.draw.rect(display,COR_PAREDE_DUNGEON,(x, y, offset, offset))
            else:
                pygame.draw.rect(display,COR_CHAO_DUNGEON,(x, y, offset, offset))

            
            #pygame.draw.circle(display,pygame.Color(255,0,0),(x+(offset/2),y+(offset/2)),3,0)

            pygame.draw.rect(display, (0,0,0), (x,y,155,155), 1) #Borda

#Construir uma dungeon
def buildDungeon(display,data):
    offset = 15
    for y in range(0,420,offset):
        for x in range(0,420,offset):
            
            dataX = floor(x/offset)
            dataY = floor(y/offset)

            if data[dataY][dataX] == 'P':
                pygame.draw.rect(display,COR_CHAO_DUNGEON,(x, y, offset, offset))
            else:
                pygame.draw.rect(display,COR_PAREDE_DUNGEON,(x, y, offset, offset))

            pygame.draw.rect(display, (0,0,0), (x,y,155,155), 1) #Borda


def mostraTexto(display,texto,top=False):
    pos = (210, 210)
    if top: pos = (210, 15)
    fontObj = pygame.font.Font('freesansbold.ttf', 12)
    textSurfaceObj = fontObj.render(texto, True, pygame.Color(0,255,0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = pos
    display.blit(textSurfaceObj, textRectObj)


def mostraAssetsMapa(display,posicaoLink, posicaoDungeon1, posicaoDungeon2, posicaoDungeon3, posicaoLostWoods, casa, espadaP):
    link = pygame.transform.scale(LINK, (10, 10))
    porta = pygame.transform.scale(PORTA, (10, 10))
    portaCasa = pygame.transform.scale(CASA, (10,10))
    espada = pygame.transform.scale(ESPADA,(10,10))

    display.blit(espada,posicaoRelativaMapa(espadaP))
    display.blit(portaCasa,posicaoRelativaMapa(casa))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon1))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon2))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon3))
    display.blit(porta,posicaoRelativaMapa(posicaoLostWoods))
    display.blit(link,posicaoRelativaMapa(posicaoLink))

def mostraAssetsDungeon(display,posicaoLink, posicaoPingente, dungeonIndex, posicaoPorta, estado):
    link = pygame.transform.scale(LINK, (15, 15))
    porta = pygame.transform.scale(PORTA, (15, 15))

    display.blit(porta,posicaoRelativaDungeon(posicaoPorta))
    display.blit(link,posicaoRelativaDungeon(posicaoLink))
    if not estado[dungeonIndex]:
        if(dungeonIndex == 0):
            display.blit(pingenteAzul,posicaoRelativaDungeon(posicaoPingente))
        elif dungeonIndex == 1:
            display.blit(pingenteVermelho,posicaoRelativaDungeon(posicaoPingente))
        else:
            display.blit(pingenteVerde,posicaoRelativaDungeon(posicaoPingente))

