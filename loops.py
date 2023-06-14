import pygame as pg 
from constantes import *
import sys
from jogo import Jogo
from final import Fim
class Loop:
    def __init__(self):
        # Inicializa o pygame
        pg.init()
        pg.display.set_caption('Desolation')
        self.window = pg.display.set_mode((LARGURA, ALTURA))
        self.jogo = Jogo()
        self.fim = Fim()
        background = pg.image.load("docs/assets/img/inicial1.png")
        self.background = pg.transform.scale(background, (LARGURA, ALTURA))
        pg.mixer.music.load("docs/assets/snd/background_music.ogg")
        pg.mixer.music.set_volume(1)
        pg.mixer.music.play(-1)

    def desenha(self):
        self.window.blit(self.background, (0, 0))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.jogo.desenha()
                        self.fim.desenha()
                        break
            pg.display.update()
           