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
        background = pg.image.load("docs/assets/img/gameover2.png")
        self.background = pg.transform.scale(background, (LARGURA, ALTURA))
    def desenha(self):
        self.window.blit(self.background, (0, 0))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pg.quit()
                        sys.exit()

            pg.display.update()