import pygame
from pygame.locals import *

ImageName = "defualtimage.png"
MaxSpeed = 3
Acc = 0.15

class Entity(object):
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

        self.surfaceObject = pygame.image.load(ImageName)
        self.width = self.surfaceObject.get_width()
        self.height = self.surfaceObject.get_height() 

    def update(self, event):

        if self.moveLeft:
            if self.xvel > -MaxSpeed:
                self.xvel -= Acc
        if self.moveRight:
            if self.xvel < MaxSpeed:
                self.xvel += Acc
        if self.moveUp:
            if self.yvel > -MaxSpeed:
                self.yvel -= Acc
        if self.moveDown:
           if self.yvel < MaxSpeed:
                self.yvel += Acc
        
        if self.moveLeft == False and self.moveRight == False:
            if self.xvel > 0:
                self.xvel -= Acc
            elif self.xvel < 0:
                self.xvel += Acc
                
        if self.moveUp == False and self.moveDown == False:
            if self.yvel > 0:
                self.yvel -= Acc
            elif self.yvel < 0:
                self.yvel += Acc
        
        self.xpos += self.xvel
        self.ypos += self.yvel
        
    def render(self, surface):
        surface.blit(self.surfaceObject, (self.xpos, self.ypos))

