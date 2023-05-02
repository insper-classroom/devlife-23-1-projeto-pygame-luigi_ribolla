import pygame as pg
import sys
from constantes import *
from objetos import Objetos
from hunter import Hunter
from settings import *
from random import choice
from arma import Arma
from dados import Dados
from monstros import Monstros

class Dungeon:
    def __init__(self):

        # guarda a janela
        self.window = pg.display.get_surface()

        # seta as sprites
        self.sprites = Camera()
        self.objetos = pg.sprite.Group()

        #ataque
        self.ataque_atual = None

        self.mapa()

        #interface
        self.dados = Dados()

    def mapa(self):
        mapas_csv = {
            "parede": importa_csv('docs/csv-map/parede.csv'),
            "hunter": importa_csv('docs/csv-map/hunter.csv'),
            "cyclope": importa_csv('docs/csv-map/cyclope.csv'),
            "fogo": importa_csv('docs/csv-map/fogo.csv'),
            "skull": importa_csv('docs/csv-map/skull.csv'),
            "beast": importa_csv('docs/csv-map/beast.csv'),
            "boss": importa_csv('docs/csv-map/boss.csv'),
             }
        
        for tipo, layout in mapas_csv.items():
            for index_linha, linha in enumerate(layout):
                for index_coluna, coluna in enumerate(linha):
                    if coluna != '-1':
                        x = index_coluna * TAMANHO_TILE
                        y = index_linha * TAMANHO_TILE
                        if tipo == "parede":
                            Objetos((x,y), ([self.objetos]), 'invisivel')
                        if tipo == "hunter":
                            if coluna == "397":
                                self.hunter = Hunter(
                                (x,y), 
                                [self.sprites],
                                self.objetos,
                                self.criar_ataque,
                                self.apagar_ataque,
                                self.criar_magia)
                        if tipo == "cyclope":
                            if coluna == "0":
                                Monstros(
                                'cyclope',
                                (x,y),
                                [self.sprites], self.objetos)
                        if tipo == "fogo":
                            if coluna == "0":
                                Monstros(
                                'fogo',
                                (x,y),
                                [self.sprites], self.objetos)
                        if tipo == "skull":
                            if coluna == "0":
                                Monstros(
                                'skull',
                                (x,y),
                                [self.sprites], self.objetos)
                        if tipo == "beast":
                            if coluna == "0":
                                Monstros(
                                'beast',
                                (x,y),
                                [self.sprites], self.objetos)

    def criar_ataque(self):
        self.ataque_atual = Arma(self.hunter,[self.sprites])

    def apagar_ataque(self):
        if self.ataque_atual:
            self.ataque_atual.kill()
        self.ataque_atual = None

    def criar_magia(self,estilo,forca,custo):
        print(estilo)
    
    def desenha(self):
        self.sprites.custom_draw(self.hunter)
        self.sprites.update()
        # self.hunter.desenha()
        self.sprites.monstro_update(self.hunter)
        self.dados.display(self.hunter)
        

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

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset = self.floor_rect.topleft - self.offset
        self.window.blit(self.floor, floor_offset)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.window.blit(sprite.image, offset_pos)

    def monstro_update(self,hunter):
        monstros_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,"tipo") and sprite.tipo == 'monstro']
        for monstro in monstros_sprites:
            monstro.monstro_update(hunter)
        
