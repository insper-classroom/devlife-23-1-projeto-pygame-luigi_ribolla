import pygame as pg
import sys
from constantes import *
from tile import Tile
from hunter import Hunter
from settings import *

class Level:
    def __init__(self):

        # guarda a janela
        self.window = pg.display.get_surface()

        # seta as sprites
        self.sprites = Camera()
        self.objetos = pg.sprite.Group()

        self.mapa()

    def mapa(self):
        layouts = {
            "limite": import_csv_layout('docs/csv-map/parede.csv'), 

        }
        for style, layout in layouts.items():
            for index_linha, linha in enumerate(layout):
                for index_coluna, coluna in enumerate(linha):
                    if coluna != '-1':
                        x = index_coluna * TAMANHO_TILE
                        y = index_linha * TAMANHO_TILE
                        if style == "limite":
                            Tile((x,y), [ self.objetos], 'invisivel')
        

        
        self.hunter = Hunter((1800,2800), [self.sprites], self.objetos)


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

        floor = pg.image.load(('docs/assets/img/mapa.png')).convert()

        self.floor = pg.transform.scale(floor, (floor.get_width() * 3, floor.get_height() * 3))
        self.floor_rect = self.floor.get_rect(topleft = (0,0))
# floor.get_width() * 2, floor.get_height() * 2
# 96 , 160
    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset = self.floor_rect.topleft - self.offset
        self.window.blit(self.floor, floor_offset)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.window.blit(sprite.image, offset_pos)

