import pygame
import Block

class blockBreaker(object):
    def __init__(self):
        self.level=1
        self.complete=False
        self.lost=False
        self.running=False
        self.block_list = pygame.sprite.RenderPlain()
        self.all_sprite_list = pygame.sprite.RenderPlain()
        
    def buildBlock(self,locations):
        for loc in locations:
            block = Block.Block((0,0,0),(20,20),loc)
            self.block_list.add(block)
            self.all_sprite_list.add(block)

    def draw(self,screen):
        self.all_sprite_list.draw(screen)
        return screen
    
    def logic(self):
        if not self.running:
            if not self.complete and not self.lost:
                if self.level==1:
                    self.buildBlock([(20,20)])
                    self.running=True

    def eventHandler(self,event):
        return True
            
        
        
