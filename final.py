import pygame as pg 
from constantes import *
import sys
from jogo import Jogo

class Fim:
    def __init__(self):
        # Inicializa o pygame
        pg.init()
        pg.display.set_caption('Desolation')
        self.window = pg.display.set_mode((LARGURA, ALTURA))

    def desenha(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pg.quit()
                        sys.exit()

            self.window.fill((0,0,0))
            pg.display.update()