import pygame
from constantes import *

class TelaInicio:
    def __init__(self):
        pygame.init()
        self.tamanho_tela = (LARGURA, ALTURA)
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.imagem_fundo = pygame.image.load("docs/assets/img/tela_inicio2.png")

    def exibir_tela(self):
        rodando = True
        while rodando:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rodando = False
                if event.type == pygame.QUIT:
                    rodando = False

            self.tela.blit(self.imagem_fundo, (0, 0))
            pygame.display.flip()