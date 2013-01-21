import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,color):
        pygame.sprite.Sprite.__init__(self)
        self.size=(80,20)
        self.image=pygame.Surface(self.size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=360
        self.rect.y=580
        self.moveLeft=False
        self.moveRight=False

    def moveEvent(self,key):
        print("in move event")
        if key == pygame.K_LEFT:
            self.moveLeft=not self.moveLeft
        elif key == pygame.K_RIGHT:
            self.moveRight=not self.moveRight

    def update(self):
        print(str(self.moveLeft)+" "+str(self.moveRight))
        if self.moveLeft:
            self.rect.x=self.rect.x-10
            if self.rect.x<0:
                self.rect.x=0
        if self.moveRight:
            self.rect.x=self.rect.x+10
            if self.rect.x>720:
                self.rect.x=720
