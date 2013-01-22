#A wrapper for pygame
#gameEngine.py
#Author: Matt Bachman
#Date:  1/20/13
#Revisions:----
#See main.py and blockBreaker.py for expamples
#Provides basic menu for game start.

#to use you must pass your custom game object into the constructor
#as myObj.  This must provide draw(self,screen), logic(self), and
#eventHandler(self,event).

#This is meant to ease in the set up of pygame games.  Just a basic
#abstraction of the pygame game loop and initialization.

#Feel free to use, please give me some props and send and email to
#mbachman1@gmail.com with GITHUB in the subject.   


import pygame
#import blockBreaker

black = ( 0, 0, 0)
white = ( 255, 255, 255)
green = ( 0, 255, 0)
red = ( 255, 0, 0)



class gameEngine(object):

    #constructor
    def __init__(self,size,name,myObj,tL=20):
        self.size=list(size)#window size
        self.name=str(name)#window name
        
        self.tickLen=tL
        self.done=False

        #menu variables
        self.startScreen=True
        self.nextLevel=False
        self.gameOver=False

        #the game
        self.game=myObj

        #pygame variables/initialization
        
        self.screen=pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        pygame.init()
        self.font = pygame.font.SysFont("ariel",25)
        self.headFont = pygame.font.SysFont("ariel",90)
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
                    test=self.menuHandler(event)
                    if test==0:
                        self.gameOver=False
                elif self.nextLevel:
                    test=self.menuHandler(event)
                    if test==0:
                        self.nextLevel=False
                else:
                    test=self.menuHandler(event)
                    if test==0:
                        self.startScreen=False
            if test==-1:
                self.done=True
                        

    def gameLogic(self):
        #no logic if the game is playing
        if not self.startScreen and not self.gameOver:
            test=self.game.logic()
            if test==1:
                self.nextLevel=True
            elif test==-1:
                self.gameOver=True
            
    def menuHandler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                self.game.nextLevel()
                return 0
            elif event.key == pygame.K_ESCAPE:
                return -1
        return 1

    def drawMenu(self,options, prompt=" "):
        title=self.headFont.render(self.name,True,white)
        self.screen.fill(black)
        self.screen.blit(title,((self.size[0]//2)-title.get_width()//2,50))
        if prompt != " ":
            prompt=self.font.render(prompt,True,white)
            self.screen.blit(prompt,
                             ((self.size[0]//2)-prompt.get_width()//2,
                              (self.size[1]//2)-prompt.get_height()//2))
        height=self.size[1]-(self.size[1]//3)
        for op in options:
            temp=self.font.render(op,True,white)
            self.screen.blit(temp,
                             ((self.size[0]//2)-temp.get_width()//2,
                              height))
            height+=(self.size[1]-(self.size[1]//3))//20
                             
    
    def gameDraw(self):
        self.screen.fill(white)
        if self.startScreen:
            self.drawMenu(("Press n for New Game","Press ESC to Quit"))
        elif self.gameOver:
            self.drawMenu(("Press n for New Game","Press ESC to Quit"),
                          "You Lose")
        elif self.nextLevel:
            self.drawMenu(("Press n for next level","Press ESC to Quit"),
                          "Way To Go")
        else:
            self.screen=self.game.draw(self.screen)
        pygame.display.flip()
    
