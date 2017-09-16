import pygame
from pygame.sprite import Sprite
from math import hypot


class BadGuy(Sprite):  # sub-class of pygame's Sprite class

    def __init__(self, screen):
        super(BadGuy, self).__init__()
        self.image = pygame.image.load('./images/monster1.png')
        self.x = 1000
        self.y = 400
        self.screen = screen
        self.speed = 4
        self.rect = self.image.get_rect()

    def update_me(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy / dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.left = self.x
        self.rect.top = self.y

    def draw_me(self):
        # self.rect.left = self.x
        # self.rect.top = self.y
        self.screen.blit(self.image, [self.x, self.y])
