# Duh....not part of core...we did $ pip install pygame

import pygame
from pygame.sprite import Group, groupcollide

# Custom Classes
from Player import Player
from BadGuy import BadGuy
from Bullet import Bullet

pygame.init()

screen_size = (1000, 800)  # immutable tuple
background_color = (82, 111, 53)  # plant v zombies color

# Create the screen to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An Epic Shooter Made with Python")

player = Player("./images/spaceGhost.png", 100, 100, screen)
badGuy = BadGuy(screen)
badGuys = Group()
badGuys.add(badGuy)

# A single bullet is created when "Fire" button pressed and it will be added to this group...
bullets = Group()  # special pygame list

game_on = True
# Set up main game loop....it runs forever!  (Until break or quit)
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 273:
                # player.y -= player.speed
                player.should_move("up", True)
            elif event.key == 274:
                # player.y += player.speed
                player.should_move("down", True)
            elif event.key == 275:
                # player.x += player.speed
                player.should_move("right", True)
            elif event.key == 276:
                # player.x -= player.speed
                player.should_move("left", True)
            elif event.key == 32:  # spacebar -- Fire!
                bullets.add(Bullet(screen, player, 1))
        elif event.type == pygame.KEYUP:
            if event.key == 273:
                # player.y -= player.speed
                player.should_move("up", False)
            elif event.key == 274:
                # player.y += player.speed
                player.should_move("down", False)
            elif event.key == 275:
                # player.x += player.speed
                player.should_move("right", False)
            elif event.key == 276:
                # player.x -= player.speed
                player.should_move("left", False)

    screen.fill(background_color)

    for badGuy in badGuys:
        badGuy.update_me(player)
        badGuy.draw_me()

    for bullet in bullets:
        # update the bullet location
        bullet.update()
        # draw the bullet
        bullet.draw_bullet()
        badGuyBulletCollisions = pygame.sprite.groupcollide(
            badGuys, bullets, True, True)

        if len(badGuyBulletCollisions) > 0:
            print "A bullet hit the monster"
        else:
            print "This bullet missed/is missing the monster"

    player.draw_me()

    pygame.display.flip()
