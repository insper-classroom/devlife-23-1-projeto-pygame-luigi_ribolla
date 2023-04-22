import pygame as pg
from constantes import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        hunter = pg.image.load('docs/assets/img/hunter.png').convert_alpha()
        self.image = pg.transform.scale(hunter, (50, 50))
        self.rect = self.image.get_rect(topleft = posicao)
        
        self.direcao = pg.math.Vector2()
        self.vel = 5
        
    def input(self):
        tecla = pg.key.get_pressed()

        if tecla[pg.K_w]:
            self.direcao.y = -1 
        elif tecla[pg.K_s]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0
        
        if tecla[pg.K_d]:
            self.direcao.x = 1
        elif tecla[pg.K_a]:
            self.direcao.x = -1
        else:
            self.direcao.x = 0

    def move(self,vel):
        self.rect.center += self.direcao * vel

    def desenha(self):
        self.input()
        self.move(self.vel)

 