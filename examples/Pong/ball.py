#ball.py
#ball class for block breaker
#Matt Bachman, Jan 2013

import pygame
import math, copy

class Ball(pygame.sprite.Sprite):
    #constructor
    def __init__(self,color,location,bSize=(10,10)):
        #inherited constructor
        pygame.sprite.Sprite.__init__(self)
        #ball variables
        self.size=bSize
        self.isMoving=False
        self.preMoveLeft=False
        self.preMoveRight=False
        self.direction=70
        self.x=float(location[0])
        self.y=float(location[1])
        self.speed=1.0
        self.lastBounce=[0,0]
        self.bounceCheck=0
        self.originalLoc=location
        #sprite variables
        self.image=pygame.Surface(self.size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        
    #for events before the ball starts moving
    def preStartMoveEvent(self,key):
        if key == pygame.K_UP:
            self.preMoveLeft=not self.preMoveLeft
        elif key == pygame.K_DOWN:
            self.preMoveRight=not self.preMoveRight
        elif key == pygame.K_RIGHT:
            self.isMoving=True
            self.preMoveLeft=False
            self.preMoveRight=False

    #move the ball with the paddle
    def preMove(self):
        if self.preMoveLeft:
            self.rect.y-=2
            if self.rect.y<35:
                self.rect.y=35
            self.y=self.rect.y
        if self.preMoveRight:
            self.rect.y+=2
            if self.rect.y>555:
                self.rect.y=555
            self.y=self.rect.y

    #horizontal bounce
    def bounce(self,diff):
        self.direction = ((180-self.direction)%360)-diff

    def bounceVert(self,diff):
        self.direction = ((360-self.direction)%360)-diff

    def reset(self):
        self.x=copy.deepcopy(self.originalLoc[0])
        self.y=copy.deepcopy(self.originalLoc[1])
        self.rect.x=self.x
        self.rect.y=self.y
        self.isMoving=False
        self.direction=75
        self.speed=1.0

    #update for sprite class
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
            elif self.y>=600:
                self.bounce(0)
                self.y=599

            if self.x <=0:
                return 0
            elif self.x>790:
                return 1

