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
#mbachman1@gmail.com with pygame_wrapper in the subject.

#Any comments/questions should be directed to the email above
#If you want to work on this with me, send me an email too.


import pygame
import pickle


##TODO MAKE COLOR DICTIONARY
#black = ( 0, 0, 0)
#white = ( 255, 255, 255)
#green = ( 0, 255, 0)
#red = ( 255, 0, 0)
color={"black":(0,0,0),"white":(255,255,255),"red":(255,0,0),"green":(0,255,0),
       "blue":(0,0,255)}



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

        #score
        self.score=0

        #pygame variables/initialization
        self.screen=pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        pygame.init()
        self.font = pygame.font.SysFont("ariel",25)
        self.headFont = pygame.font.SysFont("ariel",90)
        self.clock=pygame.time.Clock()

    #the main game loop
    def run(self):
        while not self.done:
            self.eventHandler(pygame.event.get())
            self.gameLogic()
            self.gameDraw()
            self.clock.tick(self.tickLen)
        pygame.quit()
                
    #handle pygame events
    def eventHandler(self,events):
        test=-2
        for event in events:
            handled=False
            if event.type == pygame.QUIT:
                self.done=True
                handled=True
            if not handled:
                if self.gameOver:
                    test=self.menuHandler(event)
                    if test==0:
                        self.gameOver=False
                        self.score=0
                elif self.nextLevel:
                    test=self.menuHandler(event)
                    if test==0:
                        self.nextLevel=False
                elif self.startScreen:
                    test=self.menuHandler(event)
                    if test==0:
                        self.startScreen=False
                else:
                    self.game.eventHandler(event)
            if test==-1:
                self.done=True
                        

    def gameLogic(self):
        #no logic if the game is playing
        if not self.startScreen and not self.gameOver:
            test=self.game.logic()
            if test[0]==1:
                self.nextLevel=True
            elif test[0]==-1:
                self.gameOver=True
            self.score+=test[1]
            
    def menuHandler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                self.game.nextLevel()
                return 0
            elif event.key == pygame.K_s:
                self.saveGame()
                return 4
            elif event.key == pygame.K_l:
                self.loadGame()
                return 4
            elif event.key == pygame.K_ESCAPE:
                return -1
        return 1

    def drawMenu(self,options, prompt=" "):
        title=self.headFont.render(self.name,True,color['white'])
        self.screen.fill(color['black'])
        self.screen.blit(title,((self.size[0]//2)-title.get_width()//2,50))
        if prompt !=" ":
            prompt=self.font.render(prompt,True,color['white'])
            self.screen.blit(prompt,
                             ((self.size[0]//2)-prompt.get_width()//2,
                              (self.size[1]//2)-prompt.get_height()//2))
            prompt= "Score: "+str(self.score)
            prompt=self.font.render(prompt, True, color['white'])
            self.screen.blit(prompt,
                             ((self.size[0]//2)-prompt.get_width()//2,
                              (((self.size[1]//2)+30)-prompt.get_height()//2)))
        height=self.size[1]-(self.size[1]//3)
        for op in options:
            temp=self.font.render(op,True,color['white'])
            self.screen.blit(temp,
                             ((self.size[0]//2)-temp.get_width()//2,
                              height))
            height+=(self.size[1]-(self.size[1]//3))//20
                             
    
    def gameDraw(self):
        self.screen.fill(color['white'])
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


    #TODO :: Make saveGame and loadGame platform independent
    #by removing whitespaces
    def saveGame(self):
        saveMe = (self.game.level,self.startScreen,self.nextLevel,
                  self.gameOver,self.score)
        saveFile = self.name+".pickle"
        try:
            print("Saving "+self.name)
            file = open(saveFile,'wb')
            pickle.dump(saveMe,file,pickle.HIGHEST_PROTOCOL)
            file.close()
        except:
            print("Error saving file")
            
    def loadGame(self):
        loadFile = self.name+".pickle"
        try:
            print("Loading File")
            file = open(loadFile,'rb')
            loadMe = pickle.load(file)
            file.close()
        except:
            print("Error Loading File")
        else:
            self.game.level=loadMe[0]
            self.startScreen=loadMe[1]
            self.nextLevel=loadMe[2]
            self.score=loadMe[4]
            self.gameOver=loadMe[3]
    
