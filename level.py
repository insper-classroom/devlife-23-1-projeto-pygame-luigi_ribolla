import pygame as pg
import sys
from constantes import *
from tile import Tile
from hunter import Hunter

class Level:
    def __init__(self):

        # guarda a janela
        self.window = pg.display.get_surface()

        # seta as sprites
        self.sprites = CameraY()
        self.objetos = pg.sprite.Group()

        self.mapa()

    def mapa(self):
        for index_linha, linha in enumerate(MAPA):
            for index_coluna, coluna in enumerate(linha):
                x = index_coluna * TAMANHO_TILE
                y = index_linha * TAMANHO_TILE
                if coluna == 'x':
                    Tile((x, y), [self.sprites, self.objetos])
                if coluna == 'h':
                    self.hunter = Hunter((x, y), [self.sprites], self.objetos)

    def desenha(self):
        self.sprites.custom_draw()
        self.sprites.update()
        self.hunter.desenha()

class CameraY(pg.sprite.Group):
    def __init__(self):
    
        super().__init__()
        self.window = pg.display.get_surface()
        self.offset = pg.math.Vector2(0,0)


    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.window.blit(sprite.image, offset_pos)
