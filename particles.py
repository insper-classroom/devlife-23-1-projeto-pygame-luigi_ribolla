# import pygame as pg
# from settings import *

# class AnimationPlayer:
#     def __init__(self):
#         self.frames = {
#             # magias
#             'fogo': importa_imagem('docs/assets/img/particles'),
#             'cura': importa_imagem('docs/assets/img/particles'),
#             'sagrado': importa_imagem('docs/assets/img/particles'),
#         }

#     # def create_particles(self,animation,pos,groups):
#     #     animation_frames = self.frames[animation]
#     #     ParticleEffect(pos,animation_frames,groups)

# class ParticleEffect(pg.sprite.Sprite):
#     def __init__(self, pos, animation_fames,groups):
#         super().__init__(groups)
#         self.index = 0
#         self.animation_speed = 0.1
#         self.frames = animation_fames
#         self.image = self.frames[self.index]
#         self.rect= self.image.get_rect(center = pos)

#     def animate(self):
#         self.index += self.animation_speed
#         if self.index >= len(self.frames):
#             self.kill()
#         self.image = self.frames[int(self.index)]
    
#     def update(self):
#         self.animate()