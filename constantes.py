import pygame as pg

LARGURA = 1200
ALTURA = 610
FPS = 60
TAMANHO_TILE = 48


#inimigo
dados_arma = {
    'espada1': {'cooldown': 300, 'dano': 10, 'imagem':'docs/assets/img/espadas/espada1/espada1.png'},
    'espada2': {'cooldown': 450, 'dano': 15, 'imagem':'docs/assets/img/espadas/espada2/espada2.png'}
}