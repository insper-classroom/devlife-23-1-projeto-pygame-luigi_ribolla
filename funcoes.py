import pygame as pg

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
        self.timer = pg.get_ticks()
        self.player_img = pg.transform.scale(img, (250, 250))
        self.player_hitbox = pg.get_Rect()
        self.power_use = False
        self.pos = [300, 190]
        self.vel = 0.3

    def movimento(self):
         
        tecla = pg.key.get_pressed()
        if tecla[pg.K_a] or tecla[pg.K_LEFT]:
            self.pos[0] -= self.vel
        if tecla[pg.K_d] or tecla[pg.K_RIGHT]:
            self.player_img = pg
            self.pos[0] += self.vel
        if tecla[pg.K_w] or tecla[pg.K_UP]:
            self.pos[1] -= self.vel
        if tecla[pg.K_s] or tecla[pg.K_DOWN]:
            self.pos[1] += self.vel
         
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.SPACE:
                    self.power()

        def power(self):

# class time:
#     def __init__(self):
#         self.frames = pg.get_ticks()
        
class jogo:
    def __init__(self):
        pg.init()
        largura, altura = 800, 600
        self.window = pg.display.set_mode((largura, altura))
        self.player = Player()

        self.state = {
        'mapa' : (2000,1500), # tamanho do mapa
        }

    def checa_eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        self.player.movimento()
        return True
    
    def desenha(self):
        self.window.fill((100,100,100))
        self.window.blit(self.player.player_img, self.player.pos)
        pg.display.flip()

game = jogo()

while game.checa_eventos():
    game.desenha()
