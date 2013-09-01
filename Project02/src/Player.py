import pygame
from pygame.locals import *

PlayerImageName = "cat.png"
PlayerMaxSpeed = 5
PlayerAcc = 0.25

class player:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0

        self.moveLeft = False
        self.moveUp = False
        self.moveRight = False
        self.moveDown = False

        self.surfaceObject = pygame.image.load(PlayerImageName)
        self.width = self.surfaceObject.get_width()
        self.height = self.surfaceObject.get_height() 

    def update(self, event):
        for evt in event:
            if evt.type == KEYDOWN:
                if evt.key == K_a:
                    self.moveLeft = True
                if evt.key == K_d:
                    self.moveRight = True
                if evt.key == K_s:
                    self.moveDown = True
                if evt.key == K_w:
                    self.moveUp = True
                    
            elif evt.type == KEYUP:
                if evt.key == K_a:
                    self.moveLeft = False
                if evt.key == K_d:
                    self.moveRight = False
                if evt.key == K_s:
                    self.moveDown = False
                if evt.key == K_w:
                    self.moveUp = False
        #Done with events
        
        if self.moveLeft:
            if self.xvel > -PlayerMaxSpeed:
                self.xvel -= PlayerAcc
        if self.moveRight:
            if self.xvel < PlayerMaxSpeed:
                self.xvel += PlayerAcc
        if self.moveUp:
            if self.yvel > -PlayerMaxSpeed:
                self.yvel -= PlayerAcc
        if self.moveDown:
            if self.yvel < PlayerMaxSpeed:
                self.yvel += PlayerAcc
        
        if self.moveLeft == False and self.moveRight == False:
            if self.xvel > 0:
                self.xvel -= PlayerAcc
            elif self.xvel < 0:
                self.xvel += PlayerAcc
                
        if self.moveUp == False and self.moveDown == False:
            if self.yvel > 0:
                self.yvel -= PlayerAcc
            elif self.yvel < 0:
                self.yvel += PlayerAcc
        
        self.xpos += self.xvel
        self.ypos += self.yvel
        
        if self.xpos < 0:
            self.xpos = 0
            self.xvel = 0


    def render(self, surface):
        surface.blit(self.surfaceObject, (self.xpos, self.ypos))

