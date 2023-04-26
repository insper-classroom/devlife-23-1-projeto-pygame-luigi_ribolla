
import pygame as pg
from constantes import *

class Tile(pg.sprite.Sprite):
    def __init__(self,posicao,grupos, tipo_sprite, imagem = pg.Surface((TAMANHO_TILE, TAMANHO_TILE))):
        super().__init__(grupos)

        self.tipo_sprite = tipo_sprite
        self.image = imagem
        self.rect = self.image.get_rect(topleft=posicao)
        self.hitbox = self.rect.inflate(0, -30)
