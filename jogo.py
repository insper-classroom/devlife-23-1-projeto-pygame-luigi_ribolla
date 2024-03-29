import pygame as pg
import sys
from constantes import *
from dungeon import Dungeon


class Jogo:
    def __init__(self):
        # Inicializa o pygame
        pg.init()
        pg.display.set_caption('Desolation')
        self.window = pg.display.set_mode((LARGURA, ALTURA))
        self.dungeon = Dungeon()
        self.timer = pg.time.Clock()

    def desenha(self):
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            if self.dungeon.hunter.health() == False:
                return False 
            if self.dungeon.hunter.xp == 5000:
                return False

            self.window.fill((0,0,0))
            self.dungeon.desenha()
            pg.display.update()
            self.timer.tick(FPS)