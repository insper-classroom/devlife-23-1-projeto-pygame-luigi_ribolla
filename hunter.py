import pygame as pg
from constantes import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos, objetos):
        super().__init__(grupos)
        hunter = pg.image.load('docs/assets/img/hunter.png').convert_alpha()
        self.image = pg.transform.scale(hunter, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect.inflate(0, -10)

        # animação
        self.hunter_assets()

        # movimentação
        self.direcao = pg.math.Vector2() # vetor de direção
        self.vel = 5
        self.ataque = False
        self.ataque_cooldown = 400
        self.ataque_tempo = None

        self.objetos = objetos
        
    def hunter_assets(self):
        hunter_path = 'docs/assets/img/hunter/'
        self.animations = {'cima': [], 'baixo': [], 'esquerda': [], 'direita': [],
                           'cima_ataque': [], 'baixo_ataque': [], 'esquerda_ataque': [], 'direita_ataque': [],
                           'cima_base': [], 'baixo_base': [], 'esquerda_base': [], 'direita_base': [],}

    def input(self):
        tecla = pg.key.get_pressed()
        # movimentação
        if tecla[pg.K_w]:
            self.direcao.y = -1 
        elif tecla[pg.K_s]:
            self.direcao.y = 1
        else:
            self.direcao.y = 0
        
        if tecla[pg.K_d]:
            self.direcao.x = 1
        elif tecla[pg.K_a]:
            self.direcao.x = -1
        else:
            self.direcao.x = 0
        
        if tecla[pg.K_r]:
            self.vel = 8
        else:
            self.vel = 5

        # ataque
        if tecla[pg.K_SPACE] and not self.ataque:
            self.ataque = True
            self.ataque_tempo = pg.time.get_ticks()

        # poder
        if tecla[pg.K_LSHIFT]and not self.magia:
            self.magia = True
            self.ataque_tempo = pg.time.get_ticks()

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
        t0 = pg.time.get_ticks()
        if self.ataque:
            if t0 - self.ataque_tempo >= self.ataque_cooldown:
                self.ataque = False

    def desenha(self):
        self.input()
        self.cooldown()
        self.move(self.vel)