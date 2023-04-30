import pygame as pg
from constantes import *
from settings import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos, objetos):
        super().__init__(grupos)
        self.image = pg.image.load('docs/assets/img/hunter/idle.png').convert_alpha()
        self.rect = self.image.get_rect(center = posicao)
        self.hitbox = self.rect

        # sprites
        self.sptites()
        self.estado = 'baixo'
        self.index = 0
        self.frame = 0.15

        # movimentação
        self.direcao = pg.math.Vector2()
        self.vel = 5
        self.ataque = False
        self.ataque_cooldown = 600
        self.ataque_timer = None

        self.objetos = objetos

    def sptites(self):
        pasta = 'docs/assets/img/hunter/'
        
        self.imagens = {
            "idle": (pasta + 'idle.png'),
            "attack": (pasta + 'attack.png'),
            "walk": (pasta + 'walk.png'),
        }
        self.animations = {
            'idle_baixo': [], 'idle_cima': [], 'idle_esquerda': [], 'idle_direita': [],
            'attack_baixo': [], 'attack_cima': [], 'attack_esquerda': [], 'attack_direita': [],
            'baixo': [], 'cima': [], 'esquerda': [], 'direita': [],
        }

        for sprite in self.imagens.keys():
            if sprite == 'idle':
                baixo = pg.image.load(self.imagens['idle']).subsurface([0, 0],[16, 16])
                self.animations['idle_baixo'].append(baixo)
                
                cima = pg.image.load(self.imagens['idle']).subsurface([16, 0],[16, 16])
                self.animations['idle_cima'].append(cima)
                
                esquerda = pg.image.load(self.imagens['idle']).subsurface([32, 0],[16, 16])
                self.animations['idle_esquerda'].append(esquerda)
                
                direita = pg.image.load(self.imagens['idle']).subsurface([48, 0],[16, 16])  
                self.animations['idle_direita'].append(direita)
                
                
            elif sprite == 'attack':
                baixo = pg.image.load(self.imagens['attack']).subsurface([0, 0],[16, 16])
                self.animations['attack_baixo'].append(baixo)
                
                cima = pg.image.load(self.imagens['attack']).subsurface([16, 0],[16, 16])
                self.animations['attack_cima'].append(cima)
                
                esquerda = pg.image.load(self.imagens['attack']).subsurface([32, 0],[16, 16])
                self.animations['attack_esquerda'].append(esquerda)
                
                direita = pg.image.load(self.imagens['attack']).subsurface([48, 0],[16, 16])  
                self.animations['attack_direita'].append(direita)
                
                
            elif sprite == 'walk':
                for i in range(4):
                    baixo = pg.image.load(self.imagens['walk']).subsurface([0, i*16],[16, 16])
                    self.animations['baixo'].append(baixo)
                    
                    cima = pg.image.load(self.imagens['walk']).subsurface([16, i*16],[16, 16])
                    self.animations['cima'].append(cima)
                    
                    esquerda = pg.image.load(self.imagens['walk']).subsurface([32, i*16],[16, 16])
                    self.animations['esquerda'].append(esquerda)
                    
                    direita = pg.image.load(self.imagens['walk']).subsurface([48, i*16],[16, 16])  
                    self.animations['direita'].append(direita)

    def input(self):
        tecla = pg.key.get_pressed()
        
        # movimentação 
        if tecla[pg.K_w]:
            self.direcao.y = -1 
            self.estado = 'cima'
        
        elif tecla[pg.K_s]:
            self.direcao.y = 1
            self.estado = 'baixo'
        
        else:
            self.direcao.y = 0
        
        if tecla[pg.K_d]:
            self.direcao.x = 1
            self.estado = 'direita'
        
        elif tecla[pg.K_a]:
            self.direcao.x = -1
            self.estado = 'esquerda'
        
        else:
            self.direcao.x = 0

        # ataque
        if tecla[pg.K_SPACE] and not self.ataque:
            self.ataque = True
            self.ataque_timer = pg.time.get_ticks()

        # poder
        if tecla[pg.K_LSHIFT]and not self.ataque:
            self.ataque = True
            self.ataque_timer = pg.time.get_ticks()

    def update_estado(self):
        #idle
        if self.direcao.x == 0 and self.direcao.y == 0:
            if not 'idle' in self.estado and not 'attack' in self.estado:
                self.estado = 'idle_' + self.estado

        # ataque
        if self.ataque:
            self.direcao.x = 0
            self.direcao.y = 0
            if not 'attack' in self.estado:
                if 'idle' in self.estado:
                    self.estado.replace('idle_', 'attack_')
                else:
                    self.estado = 'attack_' + self.estado

        else: 
            if 'attack' in self.estado:
                self.estado.replace('attack_', '')

    def move(self,vel):
        if self.direcao.magnitude() != 0: # se o vetor não for nulo
            self.direcao = self.direcao.normalize() # normaliza o vetor
        
        self.hitbox.x += self.direcao.x * vel
        self.collision("x")
        self.hitbox.y += self.direcao.y * vel
        self.collision("y")
        self.rect.center = self.hitbox.center

    def collision(self, direcao):
        if direcao == "x":
            for objeto in self.objetos:
                if objeto.hitbox.colliderect(self.hitbox):
                    if self.direcao.x > 0: # se estiver indo para a direita
                        self.hitbox.right = objeto.hitbox.left
                    elif self.direcao.x < 0: # se estiver indo para a esquerda
                        self.hitbox.left = objeto.hitbox.right
        if direcao == "y":
            for objeto in self.objetos:
                if objeto.hitbox.colliderect(self.hitbox):
                    if self.direcao.y > 0: # se estiver indo para baixo
                        self.hitbox.bottom = objeto.hitbox.top
                    elif self.direcao.y < 0: # se estiver indo para cima
                        self.hitbox.top = objeto.hitbox.bottom

    def cooldown(self):
        tempo_atual = pg.time.get_ticks()
        if self.ataque:
            if tempo_atual - self.ataque_timer >= self.ataque_cooldown:
                self.ataque = False               

    def animate(self):
        animacao = self.animations[self.estado]

        self.index += self.frame
        if self.index >= len(animacao):
            self.index = 0

        image = animacao[int(self.index)]
        self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def desenha(self):
        self.input()
        self.cooldown() 
        self.update_estado()
        self.animate()
        self.move(self.vel)

