import pygame

class Arbre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('apple.png')
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet, (50, 50))
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.position = [x, y]
        #self.health = health
        #self.attack = attack
        #self.sex = sex

    def update(self):
        self.rect.topleft = self.position

    def damage(self, damage):
        self.health -= damage

    def attack_carnivore(self, target_carnivore):
        target_carnivore.damage(self.attack)

    def get_image(self, x, y):
        image = pygame.Surface([128, 128])
        image.blit(self.sprite_sheet, (0,0), (x, y, 128, 128))
        return image


