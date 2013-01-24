import pygame, player

class nonPlayerCharacter(player.Player):
    def update(self,ball=None,scnSize=(800,600)):
        if ball:
            if self.direct=='vertical':
                test=self.rect.y+(self.size[1]/2)
                if ball.y>test:
                    self.rect.y=self.rect.y+1
                    atest=scnSize[1]-self.size[1]
                    if self.rect.y>atest:
                        self.rect.y=atest
                elif ball.y<test:
                    self.rect.y=self.rect.y-1
                    if self.rect.y<0:
                        self.rect.y=0
