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

def custoCaminho(caminho):
    soma = 0
    for i in caminho[1]:
        soma += i
    return soma

def proxCaminhoDungeon(mapa,posicaoLink,target,estado):
    dg1 = target[0]
    dg2 = target[1]
    dg3 = target[2]

    caminho1 = []
    caminho2 = []
    caminho3 = []

    if not estado[0]: caminho1 = buscaCaminho(mapa,posicaoLink,dg1)
    if not estado[1]: caminho2 = buscaCaminho(mapa,posicaoLink,dg2)
    if not estado[2]: caminho3 = buscaCaminho(mapa,posicaoLink,dg3)

    custo1 = sys.maxsize
    custo2 = sys.maxsize
    custo3 = sys.maxsize

    if caminho1: custo1 = custoCaminho(caminho1)
    if caminho2: custo2 = custoCaminho(caminho2)
    if caminho3: custo3 = custoCaminho(caminho3)

    menor = min(custo1,custo2,custo3)

    if menor == custo1: return caminho1
    elif menor == custo2: return caminho2
    else: return caminho3

def caminhoPingente(mapa,posicaoLink,target):
    return buscaCaminho(mapa,posicaoLink,target)

def caminhoSaida(mapa,posicaoLink,target):
    return buscaCaminho(mapa,posicaoLink,target)

def caminhoCasaLink(mapa,posicaoLink,target):
    return buscaCaminho(mapa,posicaoLink,target)
    
def caminhoLostWoods(mapa,posicaoLink,target):
    return buscaCaminho(mapa,posicaoLink,target)

def main():
    fpsClock = pygame.time.Clock()
    velocidade = 20
    total = 0

    posicaoLink = POSICAO_INICIAL

    mapa = getMapaHyrule()

    dungeons = getDungeons()
    dungeonIndex = -1
    estadoDungeons = [False, False, False] #(dungeon1, dungeon2, dungeon3)
    estadoCasaLink = False
    estadoLostWoods = False

    jogoPausado = True

    caminho = []
    custo = []

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

        if not estadoLostWoods:
            if not jogoPausado:
                if not caminho:
                    if dungeonIndex != -1:
                        if estadoDungeons[dungeonIndex] == False:
                            caminho,custo = caminhoPingente(dungeons[dungeonIndex],posicaoLink,POSICOES_PINGENTE_DUNGEON[dungeonIndex])
                        else:
                            caminho,custo = caminhoSaida(dungeons[dungeonIndex],posicaoLink, POSICOES_INICIAL_DUNGEON[dungeonIndex])
                    elif False in estadoDungeons:
                        caminho,custo = proxCaminhoDungeon(mapa,posicaoLink, POSICOES_DUNGEONS, estadoDungeons)
                    elif not estadoCasaLink:
                        caminho,custo = caminhoCasaLink(mapa,posicaoLink, POSICAO_INICIAL)
                    elif not estadoLostWoods:
                        caminho,custo = caminhoLostWoods(mapa,posicaoLink, POSICAO_LOST_WOODS)
                else:
                    posicaoLink = moveLink(caminho[0],posicaoLink)
                    if caminho[0] == posicaoLink:
                        total += custo[0]
                        caminho.remove(caminho[0])
                        custo.remove(custo[0])

                if(dungeonIndex > -1):
                    buildDungeon(DISPLAY, dungeons[dungeonIndex])
                    mostraAssetsDungeon(DISPLAY,posicaoLink,POSICOES_PINGENTE_DUNGEON[dungeonIndex],dungeonIndex,POSICOES_INICIAL_DUNGEON[dungeonIndex],estadoDungeons)
                    
                    if posicaoLink == POSICOES_PINGENTE_DUNGEON[dungeonIndex] and not estadoDungeons[dungeonIndex]:
                        estadoDungeons[dungeonIndex] = True
                    elif estadoDungeons[dungeonIndex] and posicaoLink == POSICOES_INICIAL_DUNGEON[dungeonIndex]:
                        posicaoLink = POSICOES_DUNGEONS[dungeonIndex]
                        dungeonIndex = -1
                else:
                    buildMapa(DISPLAY,mapa)
                    mostraAssetsMapa(DISPLAY,posicaoLink,POSICOES_DUNGEONS[0],POSICOES_DUNGEONS[1],POSICOES_DUNGEONS[2],POSICAO_LOST_WOODS, POSICAO_INICIAL)

                    if posicaoLink in POSICOES_DUNGEONS and not estadoDungeons[POSICOES_DUNGEONS.index(posicaoLink)]:
                        dungeonIndex = POSICOES_DUNGEONS.index(posicaoLink)
                        posicaoLink = POSICOES_INICIAL_DUNGEON[dungeonIndex]

                    if posicaoLink == POSICAO_INICIAL and not False in estadoDungeons:
                        estadoCasaLink = True
                        
                    if posicaoLink == POSICAO_LOST_WOODS and estadoCasaLink:
                        estadoLostWoods = True

        mostraPontuação(DISPLAY,total)
        if jogoPausado: mostraPause(DISPLAY)
        pygame.display.update()
        fpsClock.tick(velocidade)

if __name__ == '__main__':
    import sys
    sys.exit(main())