import pygame
import Block
import player
import ball
import sys
sys.path.append('../..')
from gameEngine import color
#Second level==JEFF

levels={"level2":[(307,80),(322,10),(322,35),(322,50),(322,65),(322,80),(342,10),(342,35),(342,50),
                      (342,65),(342,80),(357,10),(357,50),(357,80),(372,10)]}

class blockBreaker(object):
    
    def __init__(self):
        global black
        self.level=0
        self.complete=False
        self.lost=False
        
        self.block_list = pygame.sprite.RenderPlain()
        self.all_sprite_list = pygame.sprite.RenderPlain()
        self.ball_group = pygame.sprite.Group()
        self.thePlayer=player.Player(color['black'])
        self.all_sprite_list.add(self.thePlayer)
        
    def buildBlock(self,locations,color):
        for loc in locations:
            block = Block.Block(color,(20,20),loc)
            self.block_list.add(block)
            self.all_sprite_list.add(block)

    def draw(self,screen):
        self.all_sprite_list.draw(screen)
        return screen
    
    def logic(self):
            
        balls=self.ball_group.sprites()
        ballsCollide=pygame.sprite.spritecollide(self.thePlayer,
                                                 self.ball_group,False)
        if ballsCollide:
            for b in ballsCollide:
            #for i in range(len(balls)):
                diff = (self.thePlayer.rect.x + self.thePlayer.size[0]/2) - (b.rect.x+b.size[0]/2)
                ballsCollide.pop()
                b.rect.y = 600-self.thePlayer.rect.height-b.rect.height
                b.y=b.rect.y
                b.bounce(diff)
                b.lastBounce=0
        score=0
        for b in balls:
            if b.lastBounce>1000:
                b.bounce(90)
                b.lastBounce=0
            deadBlocks=pygame.sprite.spritecollide(b,self.block_list,True)
            if len(deadBlocks)>0:
                score += len(deadBlocks)*5
                b.bounce(0)
                b.lastBounce=0
        bL=self.block_list.sprites()       

        self.block_list.update()
        self.thePlayer.update()
        
        for b in balls:
            if b.update():
                self.ball_group.remove(b)
        balls=self.ball_group.sprites()
        if len(bL)==0:
            return (1,score)
        if len(balls)==0:
            return (-1,score)
        return (0,score)
            
    def nextLevel(self):
        if self.lost:
            self.level=1
        else:
            self.level+=1
        self.ball_group.empty()
        self.block_list.empty()
        self.all_sprite_list.empty()
        self.all_sprite_list.add(self.thePlayer)
        self.thePlayer.reset()
        self.buildBlock(self.buildLevel1(),color['black'])
        
    def eventHandler(self,event):
        if event.type == pygame.KEYDOWN or event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.thePlayer.moveEvent(event.key)
                aGroup=self.ball_group.sprites()
                for b in aGroup:
                    if not b.isMoving:
                        b.preStartMoveEvent(event.key)
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    aGroup=self.ball_group.sprites()
                    for b in aGroup:
                        if not b.isMoving:
                            b.preStartMoveEvent(event.key)
##            if event.type == pygame.KEYUP:
##                if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
##                    self.thePlayer.stopMove()


        
    def buildLevel1(self):
        loc=[]
        x=20
        y=80
        aBall=ball.Ball(color['red'],(395,570))
        self.all_sprite_list.add(aBall)
        self.ball_group.add(aBall)
        for i in range(120):
            if i % 30 == 0:
                x=20
                y+=25
            else:
                x+=25
            
            loc.append((x,y))
        return loc
    

    
        
        
