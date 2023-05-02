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
dados_fonte = 'docs/site/static/style/PressStart2P-Regular.ttf'
tamanho_fonte = 18

# Cores Gerais
cor_agua = '#71ddee'
cor_fundo = '#222222'
cor_borda = (30,30,30)
cor_texto = (95,211,236)

# Cores Dados
cor_vida = '#E03635'
cor_energia = '#3736B8'
cor_borda_ativacao = 'gold'

#arma
dados_arma = {
    'espada1': {'cooldown': 300, 'dano': 10, 'imagem':'docs/assets/img/espadas/espada1/espada1.png'},
    'espada2': {'cooldown': 450, 'dano': 15, 'imagem':'docs/assets/img/espadas/espada2/espada2.png'}
}

#magia
dados_magia = {
    'gelo' : {'forca': 7, 'custo':20, 'imagem':'docs/assets/img/magias/magia2/icone.png'},
    'conhecimento' : {'forca': 23, 'custo':40, 'imagem':'docs/assets/img/magias/magia1/icone.png'}
}
# inimigos 
monstros = { 
    'fogo': {'vida': 70, 'xp': 100, 'dano': 10, 'ataque': 'flam', 'som_attaque':'', 'velocidade': 3, 'resistencia': 3, 'raio_ataque': 50, 'raio_visao': 300},
    'skull': {'vida': 100, 'xp': 120, 'dano': 20, 'ataque': 'blast', 'som_attaque':'', 'velocidade': 2, 'resistencia': 3, 'raio_ataque': 60, 'raio_visao': 350},
    'beast': {'vida': 200, 'xp': 200, 'dano': 40, 'ataque': 'slash', 'som_attaque':'', 'velocidade': 1, 'resistencia': 3, 'raio_ataque': 120, 'raio_visao': 400},
    'cyclope': {'vida': 200, 'xp': 200, 'dano': 30, 'ataque': 'charge', 'som_attaque':'', 'velocidade': 2.5, 'resistencia': 3, 'raio_ataque': 70, 'raio_visao': 450},
    'boss': {'vida': 300, 'xp': 300, 'dano': 50, 'ataque': 'charge', 'som_attaque':'', 'velocidade': 1.5, 'resistencia': 3, 'raio_ataque': 120, 'raio_visao': 200},
} 