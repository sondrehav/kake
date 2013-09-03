import pygame, sys
from pygame.locals import *

from player import *
from enemy import *
from message import *

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

player = Player()
enemy = enemy()
message = msg()

player.xpos = 100
player.ypos = 100

#test:
message.out('test1')
message.out('test2')
message.out('test3')
message.out('test4')
message.setPosition(20,20)

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
            if event.key == K_F12: #Les: message.py, linje 31. Dette er midlertidig..
                message.toggle()

    player.update(events)
    enemy.update(events)
    #message.update(events)

    if player.xpos < 0:
        player.xpos = 0
        player.xvel = 0
        player.moveLeft = False
    elif player.xpos > width-player.width:
        player.xpos = width-player.width
        player.xvel =0
        player.moveRight = False
    if player.ypos < 0:
        player.ypos = 0
        player.yvel = 0
        player.yacc = 0 
    elif player.ypos > height - player.height:
        player.ypos = height - player.height
        player.yvel = 0
        player.yacc = 0


    message.render(windowSurfaceObj)
    player.render(windowSurfaceObj)
    enemy.render(windowSurfaceObj)

    pygame.display.update()
    fpsClock.tick(60) # pause to run the loop at 60 frames per second
