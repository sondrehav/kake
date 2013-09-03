import pygame
import math
from pygame.locals import *
from random import randint

class enemy:
    def __init__(self):
        self.PlayerImageName = "gun.png"
        self.xpos = 0
        self.ypos = 0
        self.vel = 0
        self.acc = 0
        self.direction = 0
        self.xdest = 0
        self.ydest = 0

        self.surfaceObject = pygame.image.load(self.PlayerImageName)
        self.width = self.surfaceObject.get_width()
        self.height = self.surfaceObject.get_height()
        
        self.state = 0
        self.getNewDest()
    def update(self, event):
        if self.state == 0: #IDLE
            if randint(0,300) == 1:
                self.getNewDest()
                self.state = 1
        if self.state == 1: #MOVING
            self.xpos += math.cos(self.direction) * self.vel
            self.ypos += math.sin(self.direction) * self.vel
            if math.sqrt(math.pow(self.xdest - self.xpos, 2) + math.pow(self.ydest - self.ypos, 2)) < 20:
                self.state = 0;
                self.vel = 0;
        #if self.state == DEAD:
        #if self.state == COMBAT:
        
    def render(self, surface):
        surface.blit(self.surfaceObject, (self.xpos, self.ypos))
    def getNewDest(self):
        self.xdest = randint(0,640)
        self.ydest = randint(0,480)
        self.direction = math.atan2((self.ydest - self.ypos), (self.xdest - self.xpos))
        self.vel = 1
        self.state = 1