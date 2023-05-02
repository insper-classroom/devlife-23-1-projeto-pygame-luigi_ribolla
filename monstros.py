import pygame as pg 
from constantes import *
from entidades import Entidades
from settings import * 

class Monstros(Entidades):
    def __init__(self, tipo, posicao, grupos, objetos, dano_player):
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
        self.dano_player = dano_player

        # invencibilidade
        self.vuneravel = True
        self.tempo_hit = None
        self.invencibilidade_cooldown = 300
    
    def graficos(self,tipo):
        
        pasta = f'docs/assets/img/monstros/{tipo}/'

        self.imagens = {
            "idle": (pasta + 'idle.png'),
            "ataque": (pasta + 'ataque.png'),
            }
        
        self.animacoes = {"idle": [], 'move': [],
                          'ataque': []}

        if tipo != 'boss':

            for sprite in range(4):
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 0],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 16],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 32],[16, 16])
                    self.animacoes['idle'].append(sprite)
                    
                    sprite = pg.image.load(self.imagens['idle']).subsurface([0, 48],[16, 16])  
                    self.animacoes['idle'].append(sprite)
        
        elif tipo == 'boss':

            for sprite in range(6):
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

            for sprite in range(6):
                sprite = pg.image.load(self.imagens['idle']).subsurface([0, 0],[160, 144])
                self.animacoes['move'].append(sprite)
                    
                sprite = pg.image.load(self.imagens['idle']).subsurface([160, 0],[160, 144])
                self.animacoes['move'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([320, 0],[160, 144])
                self.animacoes['move'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([480, 0],[160, 144])  
                self.animacoes['move'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([640, 0],[160, 144])
                self.animacoes['move'].append(sprite)
                
                sprite = pg.image.load(self.imagens['idle']).subsurface([800, 0],[160, 144])
                self.animacoes['move'].append(sprite)

            for sprite in range(11):
                sprite = pg.image.load(self.imagens['ataque']).subsurface([0, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                    
                sprite = pg.image.load(self.imagens['ataque']).subsurface([240, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([480, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([720, 0],[240, 192])  
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([960, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([1200, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)

                sprite = pg.image.load(self.imagens['ataque']).subsurface([1440, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                    
                sprite = pg.image.load(self.imagens['ataque']).subsurface([1680, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([1920, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([2160, 0],[240, 192])  
                self.animacoes['ataque'].append(sprite)
                
                sprite = pg.image.load(self.imagens['ataque']).subsurface([2400, 0],[240, 192])
                self.animacoes['ataque'].append(sprite)         
  
    def hunter_pos_dist(self, hunter):
        
        vetor_monstro = pg.math.Vector2(self.rect.center)
        vetor_hunter = pg.math.Vector2(hunter.rect.center)
        distancia = (vetor_hunter - vetor_monstro).magnitude()
        
        if distancia > 0:
            direcao = (vetor_hunter - vetor_monstro).normalize()
        else:
            direcao = pg.math.Vector2()

        return (distancia,direcao)

    def AI(self, hunter):
        distancia = self.hunter_pos_dist(hunter)[0]
        if distancia <= self.raio_ataque and self.pode_atacar:
            if self.estado != 'ataque':
                self.index = 0
            self.estado = 'ataque'
        elif distancia <= self.raio_visao:
            self.estado = 'move'
        else: 
            self.estado = 'idle'
        
    def acao(self,hunter):
        if self.estado == 'ataque':
            self.tempo_ataque = pg.time.get_ticks()
            self.dano_player(self.dano, self.ataque)
        if self.estado == 'move':
            self.direcao = self.hunter_pos_dist(hunter)[1]
        else:
            self.direcao = pg.math.Vector2()

    def animacao(self):
        if self.nome == 'boss':
            animacao = self.animacoes[self.estado]
        else:
            animacao = self.animacoes['idle']

        self.index += self.vel_frame
        if self.index >= len(animacao):
            if self.estado == "ataque":
                self.pode_atacar = False
            self.index = 0

        image = animacao[int(self.index)]
        if self.nome == 'boss':
            if self.estado == 'ataque':
                self.image = pg.transform.scale(image, (480, 384))
            else:
                self.image = pg.transform.scale(image, (320, 288))
        elif self.nome == 'fogo':
            self.image = pg.transform.scale(image, (35,35))
        elif self.nome == 'skull':
            self.image = pg.transform.scale(image, (40,40))
        else:
            self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vuneravel:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        tempo_atual = pg.time.get_ticks()
        if not self.pode_atacar:
            if tempo_atual - self.tempo_ataque >= self.ataque_cooldown:
                self.pode_atacar = True
        
        if not self.vuneravel:
            if tempo_atual - self.tempo_hit >= self.invencibilidade_cooldown:
                self.vuneravel = True

    def recebe_dano(self,hunter,tipo_ataque):
        if self.vuneravel:
            self.direcao = self.hunter_pos_dist(hunter)[1]
            if tipo_ataque == 'arma':
                self.vida -= hunter.dano_total()
            else:
                pass
                #dano magia
            self.tempo_hit = pg.time.get_ticks()
            self.vuneravel = False

    def morte(self):
        if self.vida <= 0:
            self.kill()

    def reacao(self):
        if not self.vuneravel:
            self.direcao *= - self.resistencia
   
    def update(self):
        self.reacao()
        self.move(self.vel)
        self.animacao()
        self.cooldowns()
        self.morte()

    def monstro_update(self, hunter):
        self.AI(hunter)
        self.acao(hunter)
