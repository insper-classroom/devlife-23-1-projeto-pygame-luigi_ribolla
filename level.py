import pygame as pg
import sys
from constantes import *
from tile import Tile
from hunter import Hunter
# from fire import Fire

class Level:
    def __init__(self):

        # guarda a janela
        self.window = pg.display.get_surface()

        # seta as sprites
        self.sprites = Camera()
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
        self.sprites.custom_draw(self.hunter)
        self.sprites.update()
        self.hunter.desenha()

class Camera(pg.sprite.Group):
    def __init__(self):
    
        super().__init__()
        self.window = pg.display.get_surface()
        self.half_width = self.window.get_size()[0] // 2
        self.half_height = self.window.get_size()[1] // 2
        self.offset = pg.math.Vector2()


    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.window.blit(sprite.image, offset_pos)
