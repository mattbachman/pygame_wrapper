import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,location):
        pygame.sprite.Sprite.__init__(self)
        self.size=(10,10)
        self.image=pygame.Surface(self.size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        self.isMoving=False
        self.preMoveLeft=False
        self.preMoveRight=False

    def preStartMoveEvent(self,key):
        if key == pygame.K_LEFT:
            self.preMoveLeft=not self.preMoveLeft
        elif key == pygame.K_RIGHT:
            self.preMoveRight=not self.preMoveRight
        elif key == pygame.K_UP:
            self.isMoving=True
            self.preMoveLeft=False
            self.preMoveRight=False

    def preMove(self):
        if self.preMoveLeft:
            self.rect.x=self.rect.x-10
            if self.rect.x<35:
                self.rect.x=35
        if self.preMoveRight:
            self.rect.x=self.rect.x+10
            if self.rect.x>755:
                self.rect.x=755

    def update(self):
        if not self.isMoving:
            self.preMove()
