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
    'espada1': {'cooldown': 200, 'dano': 20, 'imagem':'docs/assets/img/espadas/espada1/espada1.png'},
    'espada2': {'cooldown': 500, 'dano': 30, 'imagem':'docs/assets/img/espadas/espada2/espada2.png'},
    'cajado': {'cooldown': 450, 'dano': 60, 'imagem':'docs/assets/img/espadas/cajado/cajado.png'}
}

#magia
dados_magia = {
    'cajado' : {'forca': 7, 'custo':20, 'imagem':'docs/assets/img/espadas/cajado/cajado.png'},
}
# inimigos 
monstros = { 
    'fogo': {'vida': 120, 'xp': 80, 'dano': 30, 'ataque': 'flam', 'som_attaque':'', 'velocidade': 2.75, 'resistencia': 3, 'raio_ataque': 35, 'raio_visao': 330},
    'skull': {'vida': 180, 'xp': 120, 'dano': 40, 'ataque': 'blast', 'som_attaque':'', 'velocidade': 2, 'resistencia': 5, 'raio_ataque': 35, 'raio_visao': 350},
    'beast': {'vida': 360, 'xp': 260, 'dano': 60, 'ataque': 'slash', 'som_attaque':'', 'velocidade': 1.75, 'resistencia': 5, 'raio_ataque': 45, 'raio_visao': 400},
    'cyclope': {'vida': 300, 'xp': 260, 'dano': 50, 'ataque': 'charge', 'som_attaque':'', 'velocidade': 2.5, 'resistencia': 4, 'raio_ataque': 43, 'raio_visao': 450},
    'boss': {'vida': 2500, 'xp': 1000, 'dano': 70, 'ataque': 'charge', 'som_attaque':'', 'velocidade': 2.5, 'resistencia': - 1, 'raio_ataque': 110, 'raio_visao': 400},
} 