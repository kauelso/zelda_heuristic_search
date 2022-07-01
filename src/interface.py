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
pingenteAzul = pygame.transform.scale(pingenteAzul, (30, 30))

pingenteVermelho = pygame.image.load(assetsDir + 'pingente_vermelho.webp')
pingenteVermelho = pygame.transform.scale(pingenteVermelho, (30, 30))

pingenteVerde = pygame.image.load( assetsDir + 'pingente_verde.webp')
pingenteVerde = pygame.transform.scale(pingenteVerde, (30, 30))

def posicaoRelativaMapa(posicao):
    return ((posicao[0]*20),(posicao[1]*20))

def posicaoRelativaDungeon(posicao):
    return ((posicao[0]*30),(posicao[1]*30))

#Construir mapa de hyrule
def buildMapa(display,data):
    offset = 20
    for y in range(0,840,offset):
        for x in range(0,840,offset):
            
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
    offset = 30
    for y in range(0,840,offset):
        for x in range(0,840,offset):
            
            dataX = floor(x/offset)
            dataY = floor(y/offset)

            if data[dataY][dataX] == 'P':
                pygame.draw.rect(display,COR_CHAO_DUNGEON,(x, y, offset, offset))
            else:
                pygame.draw.rect(display,COR_PAREDE_DUNGEON,(x, y, offset, offset))

            pygame.draw.rect(display, (0,0,0), (x,y,155,155), 1) #Borda


def mostraTexto(display,texto,top=False):
    pos = (420, 420)
    if top: pos = (420, 30)
    fontObj = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObj = fontObj.render(texto, True, pygame.Color(0,255,0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = pos
    display.blit(textSurfaceObj, textRectObj)


def mostraAssetsMapa(display,posicaoLink, posicaoDungeon1, posicaoDungeon2, posicaoDungeon3, posicaoLostWoods, casa, espadaP):
    link = pygame.transform.scale(LINK, (20, 20))
    porta = pygame.transform.scale(PORTA, (20, 20))
    portaCasa = pygame.transform.scale(CASA, (20,20))
    espada = pygame.transform.scale(ESPADA,(20,20))

    display.blit(espada,posicaoRelativaMapa(espadaP))
    display.blit(portaCasa,posicaoRelativaMapa(casa))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon1))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon2))
    display.blit(porta,posicaoRelativaMapa(posicaoDungeon3))
    display.blit(porta,posicaoRelativaMapa(posicaoLostWoods))
    display.blit(link,posicaoRelativaMapa(posicaoLink))

def mostraAssetsDungeon(display,posicaoLink, posicaoPingente, dungeonIndex, posicaoPorta, estado):
    link = pygame.transform.scale(LINK, (30, 30))
    porta = pygame.transform.scale(PORTA, (30, 30))

    display.blit(porta,posicaoRelativaDungeon(posicaoPorta))
    display.blit(link,posicaoRelativaDungeon(posicaoLink))
    if not estado[dungeonIndex]:
        if(dungeonIndex == 0):
            display.blit(pingenteAzul,posicaoRelativaDungeon(posicaoPingente))
        elif dungeonIndex == 1:
            display.blit(pingenteVermelho,posicaoRelativaDungeon(posicaoPingente))
        else:
            display.blit(pingenteVerde,posicaoRelativaDungeon(posicaoPingente))

