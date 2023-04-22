
import pygame as pg
from constantes import *

class Tile(pg.sprite.Sprite):
    def __init__(self,posicao,grupos):
        super().__init__(grupos)
        self.image = pg.image.load('docs/assets/img/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=posicao)
