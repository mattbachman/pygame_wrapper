import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,color,size,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.setLocation(location)

    def setLocation(self,loc):
        self.rect.x=loc[0]
        self.rect.y=loc[1]
