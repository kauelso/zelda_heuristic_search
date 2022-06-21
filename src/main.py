from numpy import empty
import pygame, sys

from pygame.locals import *
from interface import *
from arquivos import *

POSICAO_INICIAL = (24,27)
POSICAO_LOST_WOODS = (6,5)
POSICAO_DUNGEON1 = (5,32)
POSICAO_DUNGEON2 = (39,17)
POSICAO_DUNGEON3 = (24,1)

POSICOES_INICIAL_DUNGEON = [(14,26),(13,25),(14,25)]
POSICOES_PINGENTE_DUNGEON = [(13,3),(13,3),(15,18)]

def moveLink(target, posicaoLink, velocidade):
    x = posicaoLink[0]
    y = posicaoLink[1]

    if target[0] > x:
        x = min(x + velocidade, target[0])
    elif target[0] < x:
        x = max(x - velocidade, target[0])

    if target[1] > y:
        y = min(y + velocidade, target[1])
    elif target[1] < y:
        y = max(y - velocidade, target[1])
    return (x,y)


def main():
    fpsClock = pygame.time.Clock()
    velocidade = 1
    total = 0

    posicaoLink = (27,27)

    mapa = getMapaHyrule()

    dungeons = getDungeons()
    dungeonIndex = 0
    estadoDungeons = (False, False, False) #(dungeon1, dungeon2, dungeon3)
    estadoCasaLink = False
    estadoLostWoods = False

    caminho = []

    pygame.init()

    DISPLAY = pygame.display.set_mode((840,840))
    pygame.display.set_caption('Legend of Zelda: An AI to the past')

    

    while True: #Game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
        if(not estadoLostWoods):
            if not caminho:
                if False in estadoDungeons:
                    #calculaProximoCaminhoDungeon
                    pass
                elif not estadoCasaLink:
                    #calculaCaminhoCasaLink
                    pass
                elif not estadoLostWoods:
                    #calculaCaminhoLostWoods
                    pass
                pass
            else:
                if caminho[0] == posicaoLink:
                    caminho.remove(caminho[0])
                else:
                    moveLink(caminho[0],posicaoLink,velocidade)
                pass
            if(dungeonIndex > -1):
                posicaoLink = POSICOES_INICIAL_DUNGEON[0]
                buildDungeon(DISPLAY, dungeons[dungeonIndex])
                mostraAssetsDungeon(DISPLAY,posicaoLink,(13,3),dungeonIndex)
                #calculaProximoPasso
            else:
                buildMapa(DISPLAY,mapa)
                mostraAssetsMapa(DISPLAY,posicaoLink,POSICAO_DUNGEON1,POSICAO_DUNGEON2,POSICAO_DUNGEON3,POSICAO_LOST_WOODS)
                #calculaProximoPasso       
        mostraPontuação(DISPLAY,total)
        pygame.display.update()
        fpsClock.tick(15)


if __name__ == '__main__':
    import sys
    sys.exit(main())