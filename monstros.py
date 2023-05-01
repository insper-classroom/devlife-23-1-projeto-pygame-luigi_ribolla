import pygame as pg 
from constantes import *
from entidades import Entidades
from settings import * 

class Monstros(Entidades):
    def __init__(self, tipo, posicao, grupos):
        super().__init__(grupos)
        self.sprite = 'inimigo'

        # graficos 
        self.graficos(tipo)
        self.image = pg.Surface((48,48))
        self.rect = self.image.get_rect(topleft = posicao)

    def graficos(self,nome):
        self.animacoes = {"idle": [], "move": [], "attack": []}
        
        pasta = f'docs/assets/img/monstros/{nome}/'
        for animacao in self.animacoes.keys():
            self.animacoes[animacao] = importa_imagem(pasta + animacao)
