import pygame, sys
from pygame.locals import *

from Player import *
from enemy import *

width, height = 640, 480    

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Cheat Sheet')

redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)
blackColor = pygame.Color(0, 0, 0)
mousex, mousey = 0, 0

player = player()
enemy = enemy()
player.xpos = 100
player.ypos = 100

fontObj = pygame.font.Font('freesansbold.ttf', 32)

while True:
    windowSurfaceObj.fill(whiteColor)
    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    

    player.update(events)
    enemy.update(events)

    if player.xpos < 0:
        player.xpos = 0
        player.xvel = 0
        player.moveLeft = False
    elif player.xpos > width-player.width:
        player.xpos = width-player.width
        player.xvel =0
        player.moveRight = False




    player.render(windowSurfaceObj)
    enemy.render(windowSurfaceObj)

    pygame.display.update()
    fpsClock.tick(60) # pause to run the loop at 30 frames per second
