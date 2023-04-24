
import pygame as pg
from constantes import *

class Tile(pg.sprite.Sprite):
    def __init__(self,posicao,grupos):
        super().__init__(grupos)

        image = pg.image.load('docs/assets/img/rock.png').convert_alpha()
        self.image = pg.transform.scale(image, (75, 87)).convert_alpha()
        self.rect = self.image.get_rect(topleft=posicao)
