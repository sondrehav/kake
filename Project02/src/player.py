import pygame
from pygame.locals import *
from entity import Entity

MaxSpeed = 5 #Sette inn i selve klassen?
Acc = 0.25


class Player(Entity):
    def __init__(self):
        self.imageName = "cat.png"     
        super(Player, self).__init__()

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
        super(Player, self).update(event)

    def render(self, surface):
        super(Player, self).render(surface)
