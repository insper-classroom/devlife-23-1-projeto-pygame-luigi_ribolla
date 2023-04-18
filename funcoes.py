import pygame as pg

pg.init()
largura, altura = 800, 600
window = pg.display.set_mode((largura, altura))

player_img = pg.image.load("docs/assets/img/mago.png")
player = pg.transform.scale(player_img, (250, 250))

knight_pos = [300, 190]

assets = {
   'player': player
}

state = {
    'mapa' : (2000,1500)
}

def checa_eventos():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
            
    tecla = pg.key.get_pressed()
    if tecla[pg.K_a] or tecla[pg.K_LEFT]:
        knight_pos[0] -= 0.12
    if tecla[pg.K_d] or tecla[pg.K_RIGHT]:
        knight_pos[0] += 0.12
    if tecla[pg.K_w] or tecla[pg.K_UP]:
        knight_pos[1] -= 0.12
    if tecla[pg.K_s] or tecla[pg.K_DOWN]:
        knight_pos[1] += 0.12
    return True

while checa_eventos():
    window.fill((100,100,100))
    window.blit(assets['player'], knight_pos)
    pg.display.flip()