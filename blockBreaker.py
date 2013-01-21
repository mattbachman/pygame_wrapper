import pygame
import Block
import player
import ball

    # Define some colors
black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

class blockBreaker(object):
    def __init__(self):
        global black
        self.level=1
        self.complete=False
        self.lost=False
        self.running=False
        
        self.block_list = pygame.sprite.RenderPlain()
        self.all_sprite_list = pygame.sprite.RenderPlain()
        self.ball_group = pygame.sprite.Group()
        self.thePlayer=player.Player(black)
        self.all_sprite_list.add(self.thePlayer)
        
    def buildBlock(self,locations,color):
        for loc in locations:
            block = Block.Block((0,0,0),(20,20),loc)
            self.block_list.add(block)
            self.all_sprite_list.add(block)

    def draw(self,screen):
        self.all_sprite_list.draw(screen)
        return screen
    
    def logic(self):
        global black
        if not self.running:
            if not self.complete and not self.lost:
                if self.level==1:
                    self.buildBlock(self.buildLevel1(),black)
                    self.running=True
        self.all_sprite_list.update()
            

    def eventHandler(self,event):
        if not self.running:
            if not self.complete and not self.lost:
                return True
        else:
            if event.type == pygame.KEYDOWN or event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    self.thePlayer.moveEvent(event.key)
                    aGroup=self.ball_group.sprites()
                    for b in aGroup:
                        if not b.isMoving:
                            b.preStartMoveEvent(event.key)
##            if event.type == pygame.KEYUP:
##                if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
##                    self.thePlayer.stopMove()
        return True

    def buildLevel1(self):
        global black
        loc=[]
        x=20
        y=0
        aBall=ball.Ball(black,(395,570))
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
        
        
