import pygame

class Herbivore(pygame.sprite.Sprite):
    def __init__(self, x, y, health, attack, sex, speed_x, speed_y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('rabbit.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.position = [x, y]
        self.health = health
        self.attack = attack
        self.sex = sex
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = 1

    def get_health(self):
        return self.health


    def update(self):
        self.rect.topleft = self.position

    def damage(self, damage):
        self.health -= damage

    def attack_carnivore(self, target_carnivore):
        target_carnivore.damage(self.attack)

    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0,0), (x, y, 64, 64))
        return image

    def move(self):
        if self.rect.left <= 20 or self.rect.right >= 780:
            self.direction *= -1
            self.speed_x = randint(0, 8)
            self.speed_y = randint(0, 8)

        if self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = randint(2, 8)
            self.speed_y = randint(2, 8)

        if self.rect.top <= 20 or self.rect.bottom >= 580:
            self.direction *= -1
            self.speed_x = randint(0, 8)
            self.speed_y = randint(0, 8)

        if self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = randint(2, 8)
            self.speed_y = randint(2, 8)

        self.rect.left += self.speed_x * self.direction
        self.rect.top += self.speed_y * self.direction