
import sys
sys.path.append('../..')
from gameEngine import color
import player, nonPlayer, pygame, ball


class Pong(object):
    def __init__(self,players=1):
        self.size=(800,600)
        self.players=players
        self.all_sprite_list=pygame.sprite.RenderPlain()
        self.player_list=pygame.sprite.Group()
        self.thePlayers=[]
        self.playerScore=[0,0]
        self.buildPlayers()
        self.aball=ball.Ball(color['black'],(20, self.size[1]/2 - 5))
        self.all_sprite_list.add(self.aball)
        self.font=None

    def buildPlayers(self):
        if self.thePlayers:
            del self.thePlayers
        self.thePlayers.append(player.Player(color['black'],(20,80),(0,260),'vertical'))
        if self.players == 1:
            self.thePlayers.append(nonPlayer.nonPlayerCharacter(color['black'],(20,80),(self.size[0]-20,260),
                                                            'vertical'))
            
        for i in self.thePlayers:
            self.player_list.add(i)
            self.all_sprite_list.add(i)

    def nextLevel(self):
        self.playerScore=[0,0]
        self.reset()

    def reset(self):
        self.aball.reset()
        self.resetPaddle()
        
    def resetPaddle(self):
        for i in self.thePlayers:
            i.reset()
            
    def eventHandler(self,event):
        if event.type == pygame.KEYDOWN or event.type==pygame.KEYUP:
            if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                self.thePlayers[0].moveEvent(event.key)
                if not self.aball.isMoving:
                    self.aball.preStartMoveEvent(event.key)
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    if not self.aball.isMoving:
                        self.aball.preStartMoveEvent(event.key)
    
    def draw(self,screen):
        pygame.draw.line(screen,color['black'],(self.size[0]/2,0),
                         (self.size[0]/2,self.size[1]),3)
        self.all_sprite_list.draw(screen)
        score1=self.font.render(str(self.playerScore[0]),True,color['black'])
        score2=self.font.render(str(self.playerScore[1]),True,color['black'])
        screen.blit(score1,
                    (((self.size[0]//2)-(score1.get_width()//2))-60,
                    ((self.size[1]//2)-score1.get_height()//2)//4))
        screen.blit(score2,
                    (((self.size[0]//2)-(score2.get_width()//2))+60,
                    ((self.size[1]//2)-score2.get_height()//2)//4))
        return screen
    def logic(self):
        if not self.font:
            self.font=pygame.font.SysFont("Consolas",150)
        if self.aball.isMoving:
            test=pygame.sprite.spritecollide(self.aball,self.thePlayers,False)
            if test:
                diff = (test[0].rect.y+test[0].size[1]/2)-(self.aball.rect.y+self.aball.size[1]/2)
                if test[0].rect.x==0:
                    self.aball.rect.x=self.thePlayers[0].rect.width+1
                else:
                    self.aball.rect.x=self.size[0]-self.thePlayers[0].rect.width-self.aball.rect.width
                self.aball.x=self.aball.rect.x
                self.aball.bounceVert(diff)
              
            self.thePlayers[0].update()
            self.thePlayers[1].update(self.aball)

            if self.aball.x<=0:
                self.playerScore[1]=self.playerScore[1]+1
                self.reset()
            elif self.aball.x >=780:
                self.playerScore[0]=self.playerScore[0]+1
                self.reset()
            if self.playerScore[0]==3:
                return (2,0)
            if self.playerScore[1]==3:
                return (-1,0)
        else:
            for p in self.thePlayers:
                p.update()
        self.aball.update() 
        return (0,0)
