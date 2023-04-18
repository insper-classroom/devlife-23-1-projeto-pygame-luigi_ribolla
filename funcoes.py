import pygame as pg

pg.init()
largura, altura = 800, 600
window = pg.display.set_mode((largura, altura))

player_img = pg.image.load("docs/assets/img/player.png")
player = pg.transform.scale(player_img, (50, 50))

knight_pos = [400, 300]

assets = {
   'player': player
}

def checa_eventos():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
            
    tecla = pg.key.get_pressed()
    if tecla[pg.K_a]:
        knight_pos[0] -= 0.1
    if tecla[pg.K_d]:
        knight_pos[0] += 0.1
    if tecla[pg.K_w]:
        knight_pos[1] -= 0.1
    if tecla[pg.K_s]:
        knight_pos[1] += 0.1
    return True

while checa_eventos():
    window.fill((0,0,0))
    window.blit(assets['player'], knight_pos)
    pg.display.flip()