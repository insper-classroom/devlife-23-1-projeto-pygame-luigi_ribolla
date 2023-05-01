import pygame as pg
from constantes import *

class Dados:
    def __init__(self):
        
        #geral
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(dados_fonte,tamanho_fonte)

        #barras
        self.rect_barra_vida = pg.Rect(10,10,largura_vida,altura_barra)
        self.rect_barra_energia = pg.Rect(10,35,largura_energia,altura_barra)

        # converter dicionario de armas
        self.imagem_arma = []
        for arma in dados_arma.values():
            arma_atual = arma['imagem']
            arma = pg.image.load(arma_atual).convert_alpha()
            arma = pg.transform.scale(arma,(30,50))
            self.imagem_arma.append(arma)

    def mostrar_barra(self,atual,maximo,rect_fundo,cor):
        #desenhar fundo
        pg.draw.rect(self.display_surface,cor_fundo,rect_fundo)

        # convertendo stat para pixel
        ratio = atual / maximo
        largura_atual = rect_fundo.width * ratio
        rect_atual = rect_fundo.copy()
        rect_atual.width = largura_atual

        #desenhar barra
        pg.draw.rect(self.display_surface,cor,rect_atual)
        pg.draw.rect(self.display_surface,cor_borda,rect_fundo,3)

    # def mostrar_xp(self,xp):
    #     texto_sup = self.font.render(str(int(xp)),False,cor_texto)
    #     x = self.display_surface.get_size()[0] - 20
    #     y = self.display_surface.get_size()[1] - 20
    #     texto_rect = texto_sup.get_rect(bottomright = (x,y))

    #     pg.draw.rect(self.display_surface,cor_fundo,texto_rect.inflate(10,10))
    #     self.display_surface.blit(texto_sup,texto_rect)
    #     pg.draw.rect(self.display_surface,cor_borda,texto_rect.inflate(10,10),3)

    def selecionar(self, esquerda, cima, troca):
        rect_fundo = pg.Rect(esquerda,cima,tamanho_item,tamanho_item)
        pg.draw.rect(self.display_surface,cor_fundo,rect_fundo)
        if troca:
            pg.draw.rect(self.display_surface,cor_borda_ativacao,rect_fundo,3)
        else:
            pg.draw.rect(self.display_surface,cor_borda,rect_fundo,3)
        return rect_fundo

    def sobrepor_arma(self, arma_index,troca):
        rect_fundo = self.selecionar(30,500,troca) #arma
        arma_sup = self.imagem_arma[arma_index]
        rect_arma = arma_sup.get_rect(center = rect_fundo.center)

        self.display_surface.blit(arma_sup,rect_arma)

    def display(self, hunter):
        self.mostrar_barra(hunter.vida,hunter.stats['vida'],self.rect_barra_vida,cor_vida)
        self.mostrar_barra(hunter.energia,hunter.stats['energia'],self.rect_barra_energia,cor_energia)

        # self.mostrar_xp(hunter.xp)

        self.sobrepor_arma(hunter.arma_index,not hunter.pode_trocar_arma)
        # self.selecionar(100,510,troca) magica