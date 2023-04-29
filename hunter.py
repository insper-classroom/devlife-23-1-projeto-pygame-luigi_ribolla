import pygame as pg
from constantes import *
from settings import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos, objetos):
        super().__init__(grupos)

        self.idle = True
        self.ataque = False
        self.index = 0
        self.timer = 600
        self.tempo = pg.time.get_ticks()

        # animação
        self.hunter_assets()

        # movimentação
        self.direcao = pg.math.Vector2() # vetor de direção
        self.vel = 5


        self.objetos = objetos
        # indica se o jogador está atacando
        self.ataque_tempo = pg.time.get_ticks()
        self.cooldown_atk = 5000

        self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect.inflate(0, -10)
        self.frame = 0


    def hunter_assets(self):

        hunter_sprites = "docs/assets/img/hunter/"

        self.animations = {'esquerda': [], 'direita': [],

                           'idle': [],

                           'esquerda_ataque': [], 'direita_ataque': [],

                           'esquerda_base': [], 'direita_base': [],}

        for i in range(4):
            imagem = pg.image.load('docs/assets/img/hunter/idle.png').subsurface([0, i * 24],[16, 24])
            self.animations['idle'].append(imagem)

        self.image = self.animations['idle'][self.index]

        for i in range(7):
            imagem = pg.image.load('docs/assets/img/hunter/attack.png').subsurface([0, i * 21],[31, 21])
            self.animations['direita_ataque'].append(imagem)

        self.image = self.animations['direita_ataque'][self.index]

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
            self.vel = 6
        else:
            self.vel = 4
    
        if self.ataque:
            self.idle = False
        else:
            self.idle = True

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

    # def cooldown(self):
    #     t0 = pg.time.get_ticks()
    #     if t0 - self.ataque_tempo >= self.cooldown_atk:
    #         self.ataque = False

    def desenha(self, window: pg.Surface):
        self.input()
        self.move(self.vel)
        # self.cooldown()  # chama o método cooldown antes de verificar o ataque
        if self.idle:
            self.image = self.animations['idle'][int(self.frame % len(self.animations['idle']))]
            self.image = pg.transform.scale(self.image, (48, 72))
            self.frame += 0.12
        
        if self.ataque:
            if self.frame >= len(self.animations['direita_ataque']):
                self.frame = 0
                self.ataque = False
            self.image = self.animations['direita_ataque'][int(self.frame)]
            self.image = pg.transform.scale(self.image, (96, 72))
            self.frame += 0.17
            

        pg.display.update()


