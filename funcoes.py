import pygame as pg

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
        self.player.movimento()
        return True
    
    def desenha(self):
        self.window.fill((100,100,100))
        self.window.blit(self.player.img, self.player.rect)
        for parede in self.mapa.paredes:
            self.window.blit(self.mapa.wall, (parede))
        pg.display.flip()

class Mapa:
    def __init__(self):
        self.wall = pg.image.load("docs/assets/img/wall.png")
        self.paredes = [
            pg.Rect(0, 0, 20, 600),
            pg.Rect(0, 0, 800, 20),
            pg.Rect(780, 0, 20, 600),
            pg.Rect(0, 580, 800, 20),
            pg.Rect(200, 200, 400, 200) ]


class Player:
    def __init__(self):
        self.sprites = {
            'default ': pg.image.load("docs/assets/img/hunter.png"),
            'move': pg.image.load("docs/assets/img/hunter_move_D.png"),
            'power': [],
            'attack': [],
            'morte': [],
        }
        img = pg.image.load("docs/assets/img/hunter.png")
        self.img = pg.transform.scale(img, (250, 250))
        self.rect = pg.Rect(375, 275, 250, 250)
        self.vel = (0,0)

    def movimento(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.vel[0] = -0.5
                elif event.key == pg.K_d:
                    self.vel[0] = 0.5
                elif event.key == pg.K_w:
                    self.vel[1] = -0.5
                elif event.key == pg.K_s:
                    self.vel[1] = 0.5
            elif event.type == pg.KEYUP:
                if event.key == pg.K_a and self.vel[0] < 0:
                    self.vel[0] = 0
                elif event.key == pg.K_d and self.vel[0] > 0:
                    self.vel[0] = 0
                elif event.key == pg.K_w and self.vel[1] < 0:
                    self.vel[1] = 0
                elif event.key == pg.K_s and self.vel[1] > 0:
                    self.vel[1] = 0
            
        self.rect.x += self.vel[0] 
        self.rect.y += self.vel[1]
game = Jogo()

while game.checa_eventos():
    game.desenha()
