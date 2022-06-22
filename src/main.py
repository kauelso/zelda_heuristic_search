import numpy as np
import pygame, sys

from busca.busca import buscaCaminho
from pygame.locals import *
from interface import *
from arquivos import *

POSICAO_INICIAL = (24,27)
POSICAO_LOST_WOODS = (6,5)
POSICOES_DUNGEONS = [(5,32),(39,17),(24,1)]
POSICOES_INICIAL_DUNGEON = [(14,25),(13,25),(14,25)]
POSICOES_PINGENTE_DUNGEON = [(13,3),(13,3),(15,18)]

def moveLink(target, posicaoLink):
    x = posicaoLink[0]
    y = posicaoLink[1]

    if target[0] > x:
        x = min(x + 1, target[0])
    elif target[0] < x:
        x = max(x - 1, target[0])

    if target[1] > y:
        y = min(y + 1, target[1])
    elif target[1] < y:
        y = max(y - 1, target[1])
    return (x,y)

def proxCaminhoDungeon(posicaoLink,target):
    dg1 = target[0]
    dg2 = target[1]
    dg3 = target[2]


    return []

def caminhoPingente(posicaoLink,target):
    #return caminho
    return []

def caminhoSaida(posicaoLink,target):
    #return caminho
    return []

def caminhoCasaLink(posicaoLink,target):
    #return caminho
    return []

def caminhoLostWoods(posicaoLink,target):
    #return caminho
    return []

def main():
    fpsClock = pygame.time.Clock()
    velocidade = 5
    total = 0

    posicaoLink = POSICOES_INICIAL_DUNGEON[0]

    mapa = getMapaHyrule()

    dungeons = getDungeons()
    dungeonIndex = 0
    estadoDungeons = (False, False, False) #(dungeon1, dungeon2, dungeon3)
    estadoCasaLink = False
    estadoLostWoods = False

    jogoPausado = True

    caminho = buscaCaminho(dungeons[0],posicaoLink,POSICOES_PINGENTE_DUNGEON[0])

    pygame.init()

    DISPLAY = pygame.display.set_mode((840,840))
    pygame.display.set_caption('Legend of Zelda: An AI to the past')

    

    while True: #Game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
            if event.type == KEYDOWN:
                if event.key == K_SPACE : 
                    jogoPausado = not jogoPausado

        if(not estadoLostWoods):
            if not jogoPausado:
                if not caminho:
                    if dungeonIndex != -1:
                        if estadoDungeons[dungeonIndex] == False:
                            caminho = caminhoPingente(posicaoLink,POSICOES_PINGENTE_DUNGEON[dungeonIndex])
                        else:
                            caminho = caminhoSaida(posicaoLink, POSICOES_INICIAL_DUNGEON[dungeonIndex])
                    elif False in estadoDungeons:
                        caminho = proxCaminhoDungeon(posicaoLink, POSICOES_DUNGEONS)
                    elif not estadoCasaLink:
                        caminho = caminhoCasaLink(posicaoLink, POSICAO_INICIAL)
                    elif not estadoLostWoods:
                        caminho = caminhoLostWoods(posicaoLink, POSICAO_LOST_WOODS)
                else:
                    posicaoLink = moveLink(caminho[0],posicaoLink)
                    if caminho[0] == posicaoLink:
                        caminho.remove(caminho[0])

                if(dungeonIndex > -1):
                    buildDungeon(DISPLAY, dungeons[dungeonIndex])
                    mostraAssetsDungeon(DISPLAY,posicaoLink,POSICOES_PINGENTE_DUNGEON[dungeonIndex],dungeonIndex,POSICOES_INICIAL_DUNGEON[dungeonIndex])
                    print(posicaoLink)
                    
                    if posicaoLink == POSICOES_PINGENTE_DUNGEON[dungeonIndex] and not estadoDungeons[dungeonIndex]:
                        estadoDungeons[dungeonIndex] = True
                    elif estadoDungeons[dungeonIndex] and posicaoLink == POSICOES_INICIAL_DUNGEON[dungeonIndex]:
                        posicaoLink = POSICOES_DUNGEONS[dungeonIndex]
                        dungeonIndex = -1
                else:
                    buildMapa(DISPLAY,mapa)
                    mostraAssetsMapa(DISPLAY,posicaoLink,POSICOES_DUNGEONS[0],POSICOES_DUNGEONS[1],POSICOES_DUNGEONS[2],POSICAO_LOST_WOODS)

                    if posicaoLink in POSICOES_DUNGEONS:
                        dungeonIndex = POSICOES_DUNGEONS.index(posicaoLink)
                        posicaoLink = POSICOES_INICIAL_DUNGEON[dungeonIndex]

        mostraPontuação(DISPLAY,total)
        if jogoPausado: mostraPause(DISPLAY)
        pygame.display.update()
        fpsClock.tick(velocidade)

print(buscaCaminho(getDungeons()[0],(14,25),(13,3)))

# if __name__ == '__main__':
#     import sys
#     sys.exit(main())