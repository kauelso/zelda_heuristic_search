import pygame, sys
from pygame.locals import *

COR_GRAMA = pygame.Color(146,208,80)
COR_AREIA = pygame.Color(196,188,150)
COR_FLORESTA = pygame.Color(0,176,80)
COR_MONTANHA = pygame.Color(148,138,84)
COR_AGUA = pygame.Color(84,141,212)

def buildArray(display):
    choose = 0
    for i in range(0,840,20):
        for j in range(0,840,20):
            if choose == 0:
                pygame.draw.rect(display,COR_GRAMA,(i, j, 20, 20))
            elif choose == 1:
                pygame.draw.rect(display,COR_AREIA,(i , j, 20, 20))
            elif choose == 2:
                pygame.draw.rect(display,COR_FLORESTA,(i, j , 20, 20))
            elif choose == 3:
                pygame.draw.rect(display,COR_MONTANHA,(i , j , 20, 20))
            else:
                pygame.draw.rect(display,COR_AGUA,(i , j , 20, 20))
            choose = (choose + 1) % 5



def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((840,840))
    pygame.display.set_caption('Hello World!')
    buildArray(DISPLAY)

    while True: #Game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
            pygame.display.update()

if __name__ == '__main__':
    import sys
    sys.exit(main())