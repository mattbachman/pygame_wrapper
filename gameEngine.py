#A wrapper for pygame
#gameEngine.py
#Author: Matt Bachman
#Date:  1/20/13
#Revisions:----
#To use, create a class that has a logic draw and eventHandler
#function.  See main.py and blockBreaker.py for expamples


import pygame
#import blockBreaker

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)

class gameEngine(object):
    def __init__(self,size,name,myObj,tL=20):
        self.size=list(size)
        self.name=str(name)
        self.screen=pygame.display.set_mode(size)
        self.tickLen=tL
        self.done=False
        self.startScreen=True
        self.nextLevel=False
        self.gameOver=False
        self.game=myObj
        
        pygame.display.set_caption(name)
        pygame.init()
        self.clock=pygame.time.Clock()

    def run(self):
        while not self.done:
            self.eventHandler(pygame.event.get())
            self.gameLogic()
            self.gameDraw()
            self.clock.tick()
        pygame.quit()
                

    def eventHandler(self,events):
        test=-2
        for event in events:
            handled=False
            if event.type == pygame.QUIT:
                self.done=True
                handled=True
            if not handled:
                if not self.startScreen and not self.gameOver and not self.nextLevel:
                    self.game.eventHandler(event)
                elif self.gameOver:
                    test=self.game.menuHandler(event)
                    if test==0:
                        self.gameOver=False
                elif self.nextLevel:
                    test=self.game.menuHandler(event)
                    if test==0:
                        self.nextLevel=False
                else:
                    test=self.game.menuHandler(event)
                    if test==0:
                        self.startScreen=False
            if test==-1:
                done=True
                        

    def gameLogic(self):
        if not self.startScreen and not self.gameOver:
            test=self.game.logic()
            if test==1:
                self.nextLevel=True
            elif test==-1:
                self.gameOver=True
            

    def gameDraw(self):
        self.screen.fill(white)
        self.screen=self.game.draw(self.screen)
        pygame.display.flip()
    
