import pygame, player, random

random.seed()

class nonPlayerCharacter(player.Player):
    doMove=75
    def update(self,ball=None,scnSize=(800,600)):
        if ball:
            if self.direct=='vertical':
                aTest=random.randint(0,100)
                test=self.rect.y+(self.size[1]/2)
                if aTest >=self.doMove:
                    if ball.y>scnSize[1]/2:
                        test=600
                    else:
                        test=0
                if ball.y>test:
                    self.rect.y=self.rect.y+1
                    atest=scnSize[1]-self.size[1]
                    if self.rect.y>atest:
                        self.rect.y=atest
                elif ball.y<test:
                    self.rect.y=self.rect.y-1
                    if self.rect.y<0:
                        self.rect.y=0
