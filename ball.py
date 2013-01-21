import pygame
import math

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

        self.direction=200
        self.x=float(location[0])
        self.y=float(location[1])
        self.speed=5.0

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
            self.x-=10
            if self.rect.x<35:
                self.rect.x=35
                self.x=35
        if self.preMoveRight:
            self.rect.x=self.rect.x+10
            self.x+=10
            if self.rect.x>755:
                self.rect.x=755
                self.x=755

    def bounce(self,diff):
        self.direction = ((180-self.direction)%360)-diff

    def update(self):
        if not self.isMoving:
            self.preMove()
        else:
            direction_rads=math.radians(self.direction)
            self.x+= self.speed * math.sin(direction_rads)
            self.y+= self.speed * math.cos(direction_rads)
            self.rect.x=self.x
            self.rect.y=self.y
            if self.y <=0:
                self.bounce(0)
                self.y=1
            if self.x <=0:
                self.direction=(360-self.direction)%360
                self.x=1

            if self.x>790:
                self.direction=(360-self.direction)%360
                self.x=790-1

            if self.y>600:
                return True
            else:
                return False
