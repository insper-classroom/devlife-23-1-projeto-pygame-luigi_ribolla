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
from magia import Magia
from particles import *

class Dungeon:
    def __init__(self):

        # guarda a janela
        self.window = pg.display.get_surface()

        # seta as sprites
        self.sprites = Camera()
        self.objetos = pg.sprite.Group()

        #ataque
        self.ataque_atual = None
        self.sprites_ataque = pg.sprite.Group()
        self.sprites_atacaveis = pg.sprite.Group()

        self.mapa()

        #interface
        self.dados = Dados()

        #particles 
        # self.animation_player = AnimationPlayer()
        # self.magia = Magia(self.animation_player)

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
                            if coluna != "100" and coluna != '87':
                                Objetos((x,y), ([self.objetos]), 'invisivel')
                            elif coluna == "100":
                                Objetos((x,y), ([self.sprites,self.objetos]), 'estatua', pg.image.load('docs/assets/img/estatuas/grande.png'))
                            elif coluna == '87':
                                Objetos((x,y), ([self.sprites,self.objetos]), 'sapao', pg.image.load('docs/assets/img/estatuas/sapao.png'))

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
                                [self.sprites,self.sprites_atacaveis], self.objetos, self.dano_player, self.add_xp)
                        if tipo == "fogo":
                            if coluna == "0":
                                Monstros(
                                'fogo',
                                (x,y),
                                [self.sprites,self.sprites_atacaveis], self.objetos, self.dano_player, self.add_xp)
                        if tipo == "skull":
                            if coluna == "0":
                                Monstros(
                                'skull',
                                (x,y),
                                [self.sprites,self.sprites_atacaveis], self.objetos, self.dano_player, self.add_xp)
                        if tipo == "beast":
                            if coluna == "0":
                                Monstros(
                                'beast',
                                (x,y),
                                [self.sprites,self.sprites_atacaveis], self.objetos, self.dano_player, self.add_xp)
                        if tipo == "boss":
                            if coluna == "0":
                                Monstros(
                                'boss',
                                (x,y),
                                [self.sprites,self.sprites_atacaveis], self.objetos, self.dano_player, self.add_xp)

    def criar_ataque(self):
        self.ataque_atual = Arma(self.hunter,[self.sprites,self.sprites_ataque])

    def apagar_ataque(self):
        if self.ataque_atual:
            self.ataque_atual.kill()
        self.ataque_atual = None

    def criar_magia(self,estilo,forca,custo):
        print(estilo)
        print(forca)
        print(custo)
    
    def logica_ataque_hunter(self):
        if self.sprites_ataque:
            for sprite_ataque in self.sprites_ataque:
                colisao_sprites = pg.sprite.spritecollide(sprite_ataque, self.sprites_atacaveis, False)
                if colisao_sprites:
                    for alvo in colisao_sprites:
                        if alvo.tipo == 'monstro':
                            alvo.recebe_dano(self.hunter,sprite_ataque.tipo)
                            
    def dano_player(self,dano,ataque):
        if self.hunter.vulneravel:
            self.hunter.vida -= dano
            self.hunter.vulneravel = False
            self.hunter.tempo_ataque = pg.time.get_ticks()
        # spawn particles
            # self.animation_player.create_particles(ataque, self.hunter.rect.center, [self.sprites])

    def add_xp(self,soma):
        self.hunter.xp += soma
        if self.hunter.vida < 360:
            self.hunter.vida += 2

    def desenha(self):
        self.sprites.custom_draw(self.hunter)
        self.sprites.update()
        self.sprites.monstro_update(self.hunter)
        self.logica_ataque_hunter()
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
        
