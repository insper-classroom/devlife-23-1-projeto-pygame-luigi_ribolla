import pygame as pg
import sys
from constantes import *
from dungeon import *
from jogo import *
from tela_inicio import *
from tela_fim import *


class telas:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Desolation')
        self.window = pg.display.set_mode((LARGURA, ALTURA))
        self.dungeon = Dungeon()
        self.timer = pg.time.Clock()

        self.tela_jogo = Jogo()
        self. tela_inicio = TelaInicio()
        self.tela_fim = fim()

        self.lista_telas = [self.tela_inicio, self.tela_jogo, self.tela_fim]
        self.indice_tela = 0

        def run(self):
            indice_tela = self.tela
        
