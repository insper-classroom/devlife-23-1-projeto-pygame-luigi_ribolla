import pygame as pg

LARGURA = 1200
ALTURA = 610
FPS = 60
TAMANHO_TILE = 48

# Dados
altura_barra = 20
largura_vida = 200
largura_energia = 140
tamanho_item = 80
dados_fonte = 'docs/site/static/style/Cabin_Sketch.ttf'
tamanho_fonte = 18

# Cores Gerais
cor_agua = '#71ddee'
cor_fundo = '#222222'
cor_borda = (30,30,30)
cor_texto = (255,255,255)

# Cores Dados
cor_vida = '#E03635'
cor_energia = '#3736B8'
cor_borda_ativacao = 'gold'

#inimigo
dados_arma = {
    'espada1': {'cooldown': 300, 'dano': 10, 'imagem':'docs/assets/img/espadas/espada1/espada1.png'},
    'espada2': {'cooldown': 450, 'dano': 15, 'imagem':'docs/assets/img/espadas/espada2/espada2.png'}
}

#magia
dados_magia = {
    'gelo' : {'forca': 7, 'custo':20, 'imagem':'docs/assets/img/magias/magia2/icone.png'},
    'conhecimento' : {'forca': 23, 'custo':40, 'imagem':'docs/assets/img/magias/magia1/icone.png'}
}