from csv import reader 
import pygame as pg
from os import walk 

def importa_csv(path):
    terreno = []
    with open(path) as level_map:
        layout = reader (level_map, delimiter = ',')
        for row in layout:
            terreno.append(list(row))
        return terreno
    
def importa_imagem(path):
    lista_imagens = []

    for _,__,arquivo in walk(path):
        for imagem in arquivo:
            full_path = path + '/' + imagem 
            grafico_img = pg.image.load(full_path).convert_alpha()
            lista_imagens.append(grafico_img)

    return lista_imagens

            
