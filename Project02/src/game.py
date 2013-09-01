import pygame, sys
from pygame.locals import *

width, height = 640, 480    

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Cheat Sheet')

catSurfaceObj = pygame.image.load('cat.png')
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)
blackColor = pygame.Color(0, 0, 0)
mousex, mousey = 0, 0
playerXVel, playerYVel = 0, 0
playerXPos, playerYPos = 50, 50

catMaxSpeed = 5
catAcc = 0.25

catMoveLeft, catMoveRight, catMoveUp, catMoveDown = False, False, False, False

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Katt'

while True:
    windowSurfaceObj.fill(whiteColor)

    windowSurfaceObj.blit(catSurfaceObj, (playerXPos, playerYPos))
    

    msgSurfaceObj = fontObj.render(msg, True, blueColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (width/2 - (msgRectobj.width/2), 10)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            
        elif event.type == KEYDOWN:
            if event.key == K_a:
                catMoveLeft = True
            if event.key == K_d:
                catMoveRight = True
            if event.key == K_s:
                catMoveDown = True
            if event.key == K_w:
                catMoveUp = True
                
        elif event.type == KEYUP:
            if event.key == K_a:
                catMoveLeft = False
            if event.key == K_d:
                catMoveRight = False
            if event.key == K_s:
                catMoveDown = False
            if event.key == K_w:
                catMoveUp = False
                
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    
    if catMoveLeft:
        if playerXVel > -catMaxSpeed:
            playerXVel -= catAcc
    if catMoveRight:
        if playerXVel < catMaxSpeed:
            playerXVel += catAcc
    if catMoveUp:
        if playerYVel > -catMaxSpeed:
            playerYVel -= catAcc
    if catMoveDown:
        if playerYVel < catMaxSpeed:
            playerYVel += catAcc
    
    if catMoveLeft == False and catMoveRight == False:
        if playerXVel > 0:
            playerXVel -= 0.5
        elif playerXVel < 0:
            playerXVel += 0.5
            
    if catMoveUp == False and catMoveDown == False:
        if playerYVel > 0:
            playerYVel -= 0.5
        elif playerYVel < 0:
            playerYVel += 0.5
    
    playerXPos += playerXVel
    playerYPos += playerYVel
    
    if playerXPos < 0:
        playerXPos = 0
        playerXVel = 0


    if playerXPos > width - 50:
        playerXPos = width - 50
        playerXVel = 0
    
    if playerYPos < 0:
        playerYPos = 0
        playerYVel = 0

    if playerYPos > height - 50:
        playerYPos = height - 50
        playerYVel = 0


    pygame.display.update()
    fpsClock.tick(60) # pause to run the loop at 30 frames per second
