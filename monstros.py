import pygame as pg 
from constantes import *
from entidades import Entidades
from settings import * 

class Monstros(Entidades):
    def __init__(self, tipo, posicao, grupos):
        super().__init__(grupos)
        self.tipo = tipo

        # graficos 
        self.graficos(tipo)
        self.estado = 'idle'
        image = self.animacoes[self.estado][self.index]
        self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))

        # movimentação
        self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect.inflate(0,-10)

    def graficos(self,tipo):
        
        pasta = f'docs/assets/img/monstros/{tipo}/'

        self.imagens = {
            "idle": (pasta + 'idle.png'),
            }
        
        self.animacoes = {"idle": []}
        
        for sprite in self.animacoes.keys():
                sprite = pg.image.load(self.imagens['idle']).subsurface([0, 0],[16, 16])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([16, 0],[16, 16])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([32, 0],[16, 16])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([48, 0],[16, 16])  
                self.animacoes['idle'].append(sprite)

    # def update_animacao(self):
    #     animacao = self.animations[self.estado]

    #     self.index += self.vel_frame
    #     if self.index >= len(animacao):
    #         self.index = 0

    #     image = animacao[int(self.index)]
    #     self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))
    #     self.rect = self.image.get_rect(center = self.hitbox.center)

    # def desenha(self):
    #     self.update_animacao()
