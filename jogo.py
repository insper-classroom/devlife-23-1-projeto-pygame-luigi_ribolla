import pygame as pg
import sys
from constantes import *
from level import Level

class Jogo:
    def __init__(self):

        # Inicializa o pygame
        pg.init()
        pg.display.set_caption('Desolation')
        self.window = pg.display.set_mode((LARGURA, ALTURA))
        self.level = Level()
        self.timer = pg.time.Clock()

    def desenha(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.window.fill((255,255,255))
            self.level.desenha()
            pg.display.update()
            self.timer.tick(FPS)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.desenha()