import pygame

class singleLine:
    def __init__(self, text):
        self.fontObject = pygame.font.Font('freesansbold.ttf', 16)
        self.surfaceObject = self.fontObject.render(text, True, pygame.Color(0,0,0))
        self.rectObject = self.surfaceObject.get_rect()
    def render(self, x, y, lineNumber, surface):
        self.rectObject.topleft = (x, y + (lineNumber * 20))
        surface.blit(self.surfaceObject, self.rectObject)

class msg:
    def __init__(self):
        self.lineList = []
        self.visible = False
        self.x = 10
        self.y = 10
    def out(self, text):
        self.lineList.append(singleLine(text))
    def render(self, surface):
        if self.visible:
            for i in range(0, len(self.lineList)):
                self.lineList[i].render(self.x, self.y, i, surface)
    def toggle(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False        
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False
    def setPosition(self,x,y):
        self.x = x
        self.y = y
#Hvorfor funker den ikke!?!? /rage
#    def update(self, event):
#        for evt in event:
#            if evt.type == KEYDOWN:
#                if evt.key == K_F12:
#                    if self.visible == False:
#                        self.visible = True
#                    else:
#                        self.visible = False