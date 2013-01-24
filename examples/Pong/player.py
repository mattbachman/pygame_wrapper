import pygame, copy

class Player(pygame.sprite.Sprite):
    def __init__(self,color,sz,loc,direction='horizontal'):
        pygame.sprite.Sprite.__init__(self)
        self.size=sz
        self.originalLoc=loc
        self.image=pygame.Surface(self.size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=loc[0]
        self.rect.y=loc[1]
        self.direct=direction
        self.moveLeft=False
        self.moveRight=False
        self.moveUp=False
        self.moveDown=False

    def moveEvent(self,key):
        #print("in move event")
        if self.direct=='horizontal':
            if key == pygame.K_LEFT:
                self.moveLeft=not self.moveLeft
            elif key == pygame.K_RIGHT:
                self.moveRight=not self.moveRight
        elif self.direct=='vertical':
            if key == pygame.K_UP:
                self.moveUp=not self.moveUp
            elif key == pygame.K_DOWN:
                self.moveDown=not self.moveDown
                
    def reset(self):
        self.rect.x,self.rect.y=copy.deepcopy(self.originalLoc)
        
    def update(self,ball=None,scnSize=(800,600)):
        #print(str(self.moveLeft)+" "+str(self.moveRight))
        if self.moveLeft:
            self.rect.x=self.rect.x-2
            if self.rect.x<0:
                self.rect.x=0
        if self.moveRight:
            self.rect.x=self.rect.x+2
            test=scnSize[0]-self.size[0]
            if self.rect.x>720:
                self.rect.x=720
        if self.moveUp:
            self.rect.y=self.rect.y-2
            if self.rect.y<0:
                self.rect.y=0
        if self.moveDown:
            self.rect.y=self.rect.y+2
            test=scnSize[1]-self.size[1]
            if self.rect.y>test:
                self.rect.y=test
