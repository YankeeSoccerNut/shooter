import pygame
from pygame.sprite import Sprite
from Player import Player
from JoyStick import joystick


class Bullet(Sprite):
    def __init__(self, screen, player, direction):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 20)
        self.color = (0, 0, 0)
        self.rect.centerx = player.x
        self.rect.top = player.y
        self.speed = 20
        self.direction = direction
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        # relies on transformation of booleans to decimal values and namedtuple

        # change x and y accordingly by speed....
        if self.direction == joystick.up:
            self.y -= self.speed
            self.rect.y = self.y
        elif self.direction == joystick.right:
            self.x += self.speed
            self.rect.x = self.x
        elif self.direction == joystick.down:
            self.y += self.speed
            self.rect.y = self.y
        elif self.direction == joystick.left:
            self.x -= self.speed
            self.rect.x = self.x
        elif self.direction == joystick.upright:
            self.y -= self.speed
            self.x += self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == joystick.upleft:
            self.x -= self.speed
            self.y -= self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == joystick.downright:
            self.x += self.speed
            self.y += self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == joystick.downleft:
            self.x -= self.speed
            self.y += self.speed
            self.rect.x = self.x
            self.rect.y = self.y

        if ((self.x > self.screen.get_width() or self.x < 0)
                or (self.y > self.screen.get_height() or self.y < 0)):
            print "Bullet has gone offscreen"
            self.kill()

        # # from stack overflow....didn't get it to work
        # # check if we are outside the screen...
        # if not self.game.screen.get_rect().contains(self.rect):
        #     print "Stack overflow code says offscreen too"
        #     self.kill()

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
