import pygame
import pyscroll.data
import pytmx
from pygame.locals import *
from random import randint

import carnivore
from arbre import Arbre
from carnivore import Carnivore
from herbivore import Herbivore

pygame.init()

class Eco:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Écosystème")
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer= map_layer, default_layer=1)

        self.carnivore = Carnivore(100, 100, 100, 100, 100, 5, 5)
        self.arbre = Arbre(400, 400)
        self.herbivore = Herbivore(700, 700, 100, 100, 5, 5, 5)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


        self.group.add(self.arbre)

        self.group.add(self.carnivore)
        self.group.add(self.herbivore)


    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            clock.tick(60)
            carnivore = Carnivore(100, 100, 100, 100, 100, 5, 5)
            carnivore.move()



