import pygame, sys

from pygame.locals import *
from interface import *
from arquivos import *


def main():
    mapa = getMapaHyrule()

    dungeons = getDungeons()
    dungeonIndex = 0
    estadoDungeons = (False, False, False) #(dungeon1, dungeon2, dungeon3)
    estadoCasaLink = False
    estadoLostWoods = False

    pygame.init()

    DISPLAY = pygame.display.set_mode((840,840))
    pygame.display.set_caption('Legend of Zelda: An AI to the past')

    while True: #Game loop
        for event in pygame.event.get():
            if(not estadoLostWoods):
                if(dungeonIndex > -1):
                    buildDungeon(DISPLAY, dungeons[dungeonIndex])
                    #moverLink
                    #buildDungeonAssets
                    #calculaProximoPasso
                else:
                    buildMapa(DISPLAY,mapa)
                    #moverLink
                    #buildMapAssets
                    #calculaProximoPasso
            if event.type == QUIT:
                pygame.quit()
                return 0
            pygame.display.update()


if __name__ == '__main__':
    import sys
    sys.exit(main())