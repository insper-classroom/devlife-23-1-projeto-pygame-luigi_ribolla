
import pygame as pg
from constantes import *

class Objetos(pg.sprite.Sprite):
    def __init__(self,posicao,grupos, tipo_sprite, imagem = pg.Surface((TAMANHO_TILE, TAMANHO_TILE))):
        super().__init__(grupos)

        self.tipo_sprite = tipo_sprite
        self.image = imagem
        if tipo_sprite == 'objeto':
            self.rect = self.image.get_rect(topleft = (posicao[0],posicao[1] - TAMANHO_TILE))
        elif tipo_sprite == 'estatua':
            self.image = pg.transform.scale(self.image, (TAMANHO_TILE*2, TAMANHO_TILE*3))
            self.rect = self.image.get_rect(topleft = (posicao[0],posicao[1] - TAMANHO_TILE*2))
        elif tipo_sprite == 'sapao':
            self.image = pg.transform.scale(self.image, (TAMANHO_TILE*2, TAMANHO_TILE*2))
            self.rect = self.image.get_rect(topleft = (posicao[0],posicao[1] - TAMANHO_TILE))
        else:
            self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect
