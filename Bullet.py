import pygame
from pygame.sprite import Sprite
from Player import Player


class Bullet(Sprite):
    def __init__(self, screen, player, direction):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 20)
        self.color = (0, 0, 0)
        self.rect.centerx = player.x
        self.rect.top = player.y
        self.speed = 15
        self.direction = direction
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        if self.direction == 1:  # up
            self.y -= self.speed  # change the y, each time update is run, by bullet speed
            self.rect.y = self.y  # update rect position
        elif self.direction == 2:  # right
            self.x += self.speed  # change the y, each time update is run, by bullet speed
            self.rect.x = self.x  # update rect position
        elif self.direction == 3:  # down
            self.y += self.speed  # change the y, each time update is run, by bullet speed
            self.rect.y = self.y  # update rect position
        else:  # left
            self.x -= self.speed  # change the y, each time update is run, by bullet speed
            self.rect.x = self.x  # update rect position

# print "self.x %r  self.y %r" % (self.x, self.y)
# print "get_width %r  get_height %r" % (self.screen.get_width(), self.screen.get_height())

        if ((self.x > self.screen.get_width() or self.x < 0)
                or (self.y > self.screen.get_height() or self.y < 0)):
            print "Bullet has gone offscreen"
            self.kill()

        # # from stack overflow....
        # # check if we are outside the screen...
        # if not self.game.screen.get_rect().contains(self.rect):
        #     print "Stack overflow code says offscreen too"
        #     self.kill()

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
