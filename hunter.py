import pygame as pg
from constantes import *

class Hunter:
    def __init__(self, posicao, grupos):
        super().__init__()
        self.image = pg.image.load('docs/assets/img/hunter.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=posicao)
