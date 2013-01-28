#ball.py
#ball class for block breaker
#Matt Bachman, Jan 2013

import pygame
import math

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
        #self.direction=200
        self.direction=180
        self.x=float(location[0])
        self.y=float(location[1])
        self.speed=1.2
        self.lastBounce=0

        #sprite variables
        self.image=pygame.Surface(self.size)
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=location[0]
        self.rect.y=location[1]
        
    #for events before the ball starts moving
    def preStartMoveEvent(self,key):
        if key == pygame.K_LEFT:
            self.preMoveLeft=not self.preMoveLeft
        elif key == pygame.K_RIGHT:
            self.preMoveRight=not self.preMoveRight
        elif key == pygame.K_UP:
            self.isMoving=True
            self.preMoveLeft=False
            self.preMoveRight=False

    #move the ball with the paddle
    def preMove(self):
        if self.preMoveLeft:
            self.rect.x-=1
            self.x-=1
            if self.rect.x<35:
                self.rect.x=35
                self.x=35
        if self.preMoveRight:
            self.rect.x+=1
            self.x+=1
            if self.rect.x>755:
                self.rect.x=755
                self.x=755

    #horizontal bounce
    def bounce(self,diff):
        self.direction = ((180-self.direction)%360)-diff

    #update for sprite class
    def update(self):
        if not self.isMoving:
            self.preMove()
        else:
            if self.direction>=90  and self. direction<=95:
                self.direction== 100
            elif self.direction <=270 and self.direction>=265:
                self.direction=260
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
