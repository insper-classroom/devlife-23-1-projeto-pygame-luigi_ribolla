import pygame as pg
import sys

class Jogo:
    def __init__(self):
        pg.init()
        largura, altura = 800, 600
        self.window = pg.display.set_mode((largura, altura))
        self.player = Player()
        self.mapa = Mapa()

    def checa_eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            self.player.movimento(event)
        return True
    
    def desenha(self):
        self.window.blit(self.mapa.map, (0,0))
        self.window.blit(self.player.img, self.player.rect)

        pg.display.flip()

class Mapa:
    def __init__(self):
        img = pg.image.load("docs/assets/img/backg.png")
        self.map = pg.transform.scale(img,(800,600))

class Player:
    def __init__(self):
        self.sprites = {
            'default ': pg.image.load("docs/assets/img/hunter.png"),

            'power': [],
            'attack': [],
            'morte': [],
        }
        
        img = pg.image.load("docs/assets/img/hunter.png")
        self.img = pg.transform.scale(img, (180, 180))
        self.rect = pg.Rect(350, 500, 250, 250)
        self.vel = [0,0]

    def movimento(self,event):
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                self.vel[0] = -3
            elif event.key == pg.K_d:
                self.vel[0] = 3
            elif event.key == pg.K_w:
                self.vel[1] = -3
            elif event.key == pg.K_s:
                self.vel[1] = 3

        elif event.type == pg.KEYUP:
            if event.key == pg.K_a:
                self.vel[0] = 0
            elif event.key == pg.K_d:
                self.vel[0] = 0
            elif event.key == pg.K_w:
                self.vel[1] = 0
            elif event.key == pg.K_s:
                self.vel[1] = 0
            
        self.rect.x += self.vel[0] 
        self.rect.y += self.vel[1]

game = Jogo()

while game.checa_eventos():
    game.desenha()
