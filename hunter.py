import pygame as pg
from constantes import *
from settings import *
from entidades import Entidades

class Hunter(Entidades):
    def __init__(self, posicao, grupos, objetos,criar_ataque,apagar_ataque,criar_magia):
        super().__init__(grupos)
        self.image = pg.image.load('docs/assets/img/hunter/idle.png').convert_alpha()
        self.rect = self.image.get_rect(center = posicao)
        self.hitbox = self.rect

        # sprites
        self.sprites()
        self.estado = 'baixo'


        # movimentação

        self.ataque = False
        self.ataque_cooldown = 150
        self.ataque_timer = None

        self.objetos = objetos

        # arma
        self.criar_ataque = criar_ataque
        self.apagar_ataque = apagar_ataque
        self.arma_index = 0
        self.arma = list(dados_arma.keys())[self.arma_index]
        self.pode_trocar_arma = True
        self.tempo_troca = None
        self.trocar_duracao_cooldown = 200

        #magia
        self.criar_magia = criar_magia
        self.magia_index = 0
        self.magia = list(dados_magia.keys())[self.magia_index]
        self.pode_trocar_magia = True
        self.tempo_troca_magia = None

        #stats
        self.stats = {'vida': 100,'energia': 100, 'dano': 10, 'magia': 5, 'velocidade': 4}
        self.vida = self.stats['vida'] 
        self.energia = self.stats['energia']
        self.vel = self.stats['velocidade']
        self.xp = 10
        
    def sprites(self):
        pasta = 'docs/assets/img/hunter/'
        
        self.imagens = {
            "idle": (pasta + 'idle.png'),
            "attack": (pasta + 'attack.png'),
            "walk": (pasta + 'walk.png'),
        }
        self.animations = {
            'idle_baixo': [], 'idle_cima': [], 'idle_esquerda': [], 'idle_direita': [],
            'attack_baixo': [], 'attack_cima': [], 'attack_esquerda': [], 'attack_direita': [],
            'baixo': [], 'cima': [], 'esquerda': [], 'direita': [],
        }

        for sprite in self.imagens.keys():
            if sprite == 'idle':
                baixo = pg.image.load(self.imagens['idle']).subsurface([0, 0],[16, 16])
                self.animations['idle_baixo'].append(baixo)
                
                cima = pg.image.load(self.imagens['idle']).subsurface([16, 0],[16, 16])
                self.animations['idle_cima'].append(cima)
                
                esquerda = pg.image.load(self.imagens['idle']).subsurface([32, 0],[16, 16])
                self.animations['idle_esquerda'].append(esquerda)
                
                direita = pg.image.load(self.imagens['idle']).subsurface([48, 0],[16, 16])  
                self.animations['idle_direita'].append(direita)
                
                
            elif sprite == 'attack':
                baixo = pg.image.load(self.imagens['attack']).subsurface([0, 0],[16, 16])
                self.animations['attack_baixo'].append(baixo)
                
                cima = pg.image.load(self.imagens['attack']).subsurface([16, 0],[16, 16])
                self.animations['attack_cima'].append(cima)
                
                esquerda = pg.image.load(self.imagens['attack']).subsurface([32, 0],[16, 16])
                self.animations['attack_esquerda'].append(esquerda)
                
                direita = pg.image.load(self.imagens['attack']).subsurface([48, 0],[16, 16])  
                self.animations['attack_direita'].append(direita)
                
                
            elif sprite == 'walk':
                for i in range(4):
                    baixo = pg.image.load(self.imagens['walk']).subsurface([0, i*16],[16, 16])
                    self.animations['baixo'].append(baixo)
                    
                    cima = pg.image.load(self.imagens['walk']).subsurface([16, i*16],[16, 16])
                    self.animations['cima'].append(cima)
                    
                    esquerda = pg.image.load(self.imagens['walk']).subsurface([32, i*16],[16, 16])
                    self.animations['esquerda'].append(esquerda)
                    
                    direita = pg.image.load(self.imagens['walk']).subsurface([48, i*16],[16, 16])  
                    self.animations['direita'].append(direita)

    def input(self):
        tecla = pg.key.get_pressed()
        
        # movimentação 
        if self.ataque == False:
            if tecla[pg.K_w]:
                self.direcao.y = -1 
                self.estado = 'cima'
            
            elif tecla[pg.K_s]:
                self.direcao.y = 1
                self.estado = 'baixo'
            
            else:
                self.direcao.y = 0
            
            if tecla[pg.K_d]:
                self.direcao.x = 1
                self.estado = 'direita'
            
            elif tecla[pg.K_a]:
                self.direcao.x = -1
                self.estado = 'esquerda'
            
            else:
                self.direcao.x = 0

            # ataque
            if tecla[pg.K_SPACE]:
                self.ataque = True
                self.ataque_timer = pg.time.get_ticks()
                self.criar_ataque()

            # magia
            if tecla[pg.K_LSHIFT]:
                self.ataque = True
                self.ataque_timer = pg.time.get_ticks()
                estilo = list(dados_magia.keys())[self.magia_index]
                forca = list(dados_magia.values())[self.magia_index]['forca'] + self.stats['magia']
                custo = list(dados_magia.values())[self.magia_index]['custo']
                self.criar_magia(estilo,forca,custo)

            if tecla[pg.K_k] and self.pode_trocar_arma:
                self.pode_trocar_arma = False
                self.tempo_troca = pg.time.get_ticks()
                if self.arma_index == 0:
                    self.arma_index = 1
                    self.arma = list(dados_arma.keys())[self.arma_index]
                elif self.arma_index == 1:
                    self.arma_index = 0
                    self.arma = list(dados_arma.keys())[self.arma_index]

            if tecla[pg.K_m] and self.pode_trocar_magia:
                self.pode_trocar_magia = False
                self.tempo_troca_magia = pg.time.get_ticks()
                if self.magia_index == 0:
                    self.magia_index = 1
                    self.magia = list(dados_magia.keys())[self.magia_index]
                elif self.magia_index == 1:
                    self.magia_index = 0
                    self.magia = list(dados_magia.keys())[self.magia_index]

    def update_estado(self):
        #idle
        if self.direcao.x == 0 and self.direcao.y == 0:
            if not 'idle' in self.estado and not 'attack' in self.estado:
                self.estado = 'idle_' + self.estado

        # ataque
        if self.ataque:
            self.direcao.x = 0
            self.direcao.y = 0
            if 'attack' not in self.estado:
                if 'idle' in self.estado:
                    self.estado = self.estado.replace('idle_', 'attack_')
                else:
                    self.estado = 'attack_' + self.estado

        else: 
            if 'attack' in self.estado:
                self.estado = self.estado.replace('attack_', '')

    def move(self,vel):
        if self.direcao.magnitude() != 0: # se o vetor não for nulo
            self.direcao = self.direcao.normalize() # normaliza o vetor
        
        self.hitbox.x += self.direcao.x * vel
        self.collision("x")
        self.hitbox.y += self.direcao.y * vel
        self.collision("y")
        self.rect.center = self.hitbox.center

    def collision(self, direcao):
        if direcao == "x":
            for objeto in self.objetos:
                if objeto.hitbox.colliderect(self.hitbox):
                    if self.direcao.x > 0: # se estiver indo para a direita
                        self.hitbox.right = objeto.hitbox.left
                    elif self.direcao.x < 0: # se estiver indo para a esquerda
                        self.hitbox.left = objeto.hitbox.right
        if direcao == "y":
            for objeto in self.objetos:
                if objeto.hitbox.colliderect(self.hitbox):
                    if self.direcao.y > 0: # se estiver indo para baixo
                        self.hitbox.bottom = objeto.hitbox.top
                    elif self.direcao.y < 0: # se estiver indo para cima
                        self.hitbox.top = objeto.hitbox.bottom

    def cooldown(self):
        tempo_atual = pg.time.get_ticks()

        if self.ataque:
            if tempo_atual - self.ataque_timer >= self.ataque_cooldown + dados_arma[self.arma]['cooldown']:
                self.ataque = False
                self.apagar_ataque()               

        if not self.pode_trocar_arma:
            if tempo_atual - self.tempo_troca >= self.trocar_duracao_cooldown:
                self.pode_trocar_arma = True

        if not self.pode_trocar_magia:
            if tempo_atual - self.tempo_troca_magia >= self.trocar_duracao_cooldown:
                self.pode_trocar_magia = True

    def update_animacao(self):
        animacao = self.animations[self.estado]

        self.index += self.vel_frame
        if self.index >= len(animacao):
            self.index = 0

        image = animacao[int(self.index)]
        self.image = pg.transform.scale(image, (TAMANHO_TILE, TAMANHO_TILE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def dano_total(self):
        dano_base = self.stats['dano']
        dano_arma = dados_arma[self.arma]['dano']

        return dano_base + dano_arma

    def update(self):
        self.input()
        self.cooldown() 
        self.update_estado()
        self.update_animacao()
        self.move(self.vel)