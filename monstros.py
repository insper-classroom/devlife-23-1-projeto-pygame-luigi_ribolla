import pygame as pg 
from constantes import *
from entidades import Entidades
from settings import * 

class Monstros(Entidades):
    def __init__(self, tipo, posicao, grupos, objetos):
        super().__init__(grupos)
        self.tipo = "monstro"
        self.nome = tipo

        # graficos 
        self.graficos(tipo)
        self.estado = 'idle'
        image = self.animacoes[self.estado][self.index]
        self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))

        # movimentação
        self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect.inflate(0,-10)
        self.objetos = objetos

        #características
        self.nome = tipo
        info = monstros[self.nome]
        self.vida = info['vida']
        self.xp = info["xp"]
        self.dano = info["dano"]
        self.vel = info["velocidade"]
        self.resistencia = info["resistencia"]
        self.raio_ataque = info["raio_ataque"]
        self.raio_visao = info["raio_visao"]
        self.ataque = info["ataque"]

        # intersação com o player
        self.pode_atacar = True 
        self.tempo_ataque = None
        self.ataque_cooldown = 500

    
    def graficos(self,tipo):
        
        pasta = f'docs/assets/img/monstros/{tipo}/'

        self.imagens = {
            "idle": (pasta + 'idle.png'),
            }
        
        self.animacoes = {"idle": []}

        if tipo != 'boss':

            for sprite in self.animacoes.keys():
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 0],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 16],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 32],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 48],[16, 16])  
                    self.animacoes['idle'].append(sprite)
        
        if tipo == 'boss':

            for sprite in self.animacoes.keys():
                sprite = pg.image.load(self.imagens['idle']).subsurface([0, 0],[160, 144])
                self.animacoes['idle'].append(sprite)
                    
                sprite = pg.image.load(self.imagens['idle']).subsurface([160, 0],[160, 144])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([320, 0],[160, 144])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([480, 0],[160, 144])  
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([640, 0],[160, 144])
                self.animacoes['idle'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([800, 0],[160, 144])
                self.animacoes['idle'].append(sprite)

    
    def hunter_pos_dist(self, hunter):
        vetor_monstro = pg.math.Vector2(self.rect.center)
        vetor_hunter = pg.math.Vector2(hunter.rect.center)
        distancia = (vetor_hunter - vetor_monstro).magnitude()
        
        if distancia > 0:
            direcao =  (vetor_hunter - vetor_monstro).normalize()
        else:
            direcao = pg.math.Vector2()

        return (distancia,direcao)

    def AI(self, hunter):
        distancia = self.hunter_pos_dist(hunter)[0]
        if distancia <= self.raio_ataque and self.pode_atacar:
            if self.estado != 'ataque':
                self.index = 0
            self.estado = 'ataque'
            self.pode_atacar = False
            self.tempo_ataque = pg.time.get_ticks()
            print('ataque')
        elif distancia <= self.raio_visao:
            self.estado = 'move'
        else: 
            self.estado = 'idle'
        
    def acao(self,hunter):
        # if self.estado == 'ataque':
        if self.estado == 'move':
            self.direcao = self.hunter_pos_dist(hunter)[1]
        else:
            self.direcao = pg.math.Vector2()

    def animacao(self):
        animacao = self.animacoes['idle']

        self.index += self.vel_frame
        if self.index >= len(animacao):
            if self.estado == 'ataque':
                self.pode_atacar = False
                print('False')
            self.index = 0

        image = animacao[int(self.index)]
        if self.nome == 'boss':
            self.image = pg.transform.scale(image, (320, 288))
        elif self.nome == 'fogo':
            self.image = pg.transform.scale(image, (35,35))
        elif self.nome == 'skull':
            self.image = pg.transform.scale(image, (40,40))
        else:
            self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldown(self):
        if not self.pode_atacar:
            tempo_atual = pg.time.get_ticks()
            if tempo_atual - self.tempo_ataque >= self.ataque_cooldown:
                self.pode_atacar = True

    def update(self):
        self.move(self.vel)
        self.animacao()
        self.cooldown()

    def monstro_update(self, hunter):
        self.AI(hunter)
        self.acao(hunter)
