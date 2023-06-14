import pygame as pg
from math import sin
class Entidades(pg.sprite.Sprite): 
    def __init__(self,groups):
        super().__init__(groups)

        self.index = 0
        self.vel_frame = 0.13
        self.direcao = pg.math.Vector2()

    def move(self,vel):
        if self.direcao.magnitude() != 0: # se o vetor não for nulo
            self.direcao = self.direcao.normalize() # normaliza o vetor
        
        self.hitbox.x += self.direcao.x * vel
        if self.nome != "boss":
            self.collision("x")
        self.hitbox.y += self.direcao.y * vel
        if self.nome != "boss":
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
    
    def wave_value(self):
        value = sin(pg.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0
