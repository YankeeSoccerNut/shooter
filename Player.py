import pygame
from pygame.sprite import Sprite


class Player(Sprite):  # sub-class of pygame's Sprite class
    def __init__(self, image, start_x, start_y, screen):
        super(Player, self).__init__()  # remember to call the super class
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (80, 90))
        self.x = start_x
        self.y = start_y
        self.speed = 10
        self.screen = screen
        self.should_move_up = False
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.rect = self.image.get_rect()
        print "Player Height %r, Player width %r" % (self.rect.height, self.rect.width)

    def draw_me(self):

        if(self.should_move_up and (self.y > 0)):
            self.y -= self.speed
        elif(self.should_move_down and (self.y < self.screen.get_height() - self.rect.height)):
            self.y += self.speed

        if(self.should_move_left and (self.x > 0)):
            self.x -= self.speed
        elif(self.should_move_right and (self.x < self.screen.get_width() - self.rect.width)):
            self.x += self.speed

        self.screen.blit(self.image, [self.x, self.y])

    def should_move(self, direction, yes_or_no):
        if(direction == "up"):
            self.should_move_up = yes_or_no
        if(direction == "down"):
            self.should_move_down = yes_or_no
        if(direction == "left"):
            self.should_move_left = yes_or_no
        if(direction == "right"):
            self.should_move_right = yes_or_no
