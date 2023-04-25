import pygame as pg
from constantes import *

class Hunter(pg.sprite.Sprite):
    def __init__(self, posicao, grupos, objetos):
        super().__init__(grupos)
        hunter = pg.image.load('docs/assets/img/hunter.png').convert_alpha()
        self.image = pg.transform.scale(hunter, (38, 38))
        self.rect = self.image.get_rect(topleft = posicao)
        self.hitbox = self.rect.inflate(0, -10)
        
        self.direcao = pg.math.Vector2() # vetor de direção
        self.vel = 5
        self.objetos = objetos
        
    def input(self):
        tecla = pg.key.get_pressed()

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

    def desenha(self):
        self.input()
        self.move(self.vel)

 