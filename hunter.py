import pygame as pg
from constantes import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        hunter = pg.image.load('docs/assets/img/hunter.png').convert_alpha()
        self.image = pg.transform.scale(hunter, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(topleft=posicao)
