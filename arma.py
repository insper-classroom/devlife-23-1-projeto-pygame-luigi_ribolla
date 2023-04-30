import pygame as pg

class Arma(pg.sprite.Sprite):
    def __init__(self,hunter,grupos):
        super().__init__(grupos)
        direcao = hunter.estado.split('_')[0]

        #gráfico
        imagens_gerais = f'docs/assets/img/espadas/{hunter.arma}/{direcao}.png'
        self.image = pg.image.load(imagens_gerais).convert_alpha()

        # mudança de escala dependendo da direção, vertical ou horizontal
        if direcao == 'esquerda' or direcao == 'direita':
            self.image = pg.transform.scale(self.image,(30,20))
        else:
            self.image = pg.transform.scale(self.image,(20,30))

        #posição
        if direcao == 'direita':
            self.rect = self.image.get_rect(midleft = hunter.rect.midright + pg.math.Vector2(0,11))

        elif direcao == 'esquerda':
            self.rect = self.image.get_rect(midright = hunter.rect.midleft + pg.math.Vector2(0,11))

        elif direcao == 'baixo':
            self.rect = self.image.get_rect(midtop = hunter.rect.midbottom + pg.math.Vector2(-10,0))

        elif direcao == 'cima':
            self.rect = self.image.get_rect(midbottom = hunter.rect.midtop + pg.math.Vector2(-10,0))