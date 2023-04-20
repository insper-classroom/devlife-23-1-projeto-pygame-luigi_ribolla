import pygame as pg
import sys
from constantes import *

class Jogo:
    def __init__(self):

        # Inicializa o pygame
        pg.init()
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption('Hitto')
        self.timer = pg.time.Clock()

    def atualiza(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.tela.fill((0, 0, 0))
            pg.display.update()
            self.timer.tick(FPS)

if __name__ == '__main__':
    Jogo().atualiza()