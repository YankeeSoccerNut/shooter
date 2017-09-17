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
        self.speed = 20
        self.direction = direction
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        if self.direction == 16:  # up
            self.y -= self.speed  # change the y, each time update is run, by bullet speed
            self.rect.y = self.y  # update rect position
        elif self.direction == 1:  # right
            self.x += self.speed  # change the y, each time update is run, by bullet speed
            self.rect.x = self.x  # update rect position
        elif self.direction == 8:  # down
            self.y += self.speed  # change the y, each time update is run, by bullet speed
            self.rect.y = self.y  # update rect position
        elif self.direction == 4:  # left
            self.x -= self.speed  # change the y, each time update is run, by bullet speed
            self.rect.x = self.x  # update rect position
        elif self.direction == 17:  # up and right
            self.y -= self.speed
            self.x += self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == 20:  # up and left
            self.x -= self.speed
            self.y -= self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == 9:  # down and right
            self.x += self.speed
            self.y += self.speed
            self.rect.x = self.x
            self.rect.y = self.y
        elif self.direction == 12:  # down and left
            self.x -= self.speed
            self.y += self.speed
            self.rect.x = self.x
            self.rect.y = self.y

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
