#basic driver for implementation of gameEngine.py
#Matt Bachman, Jan 2013

import sys
sys.path.append('../..')
from gameEngine import gameEngine
import pong

def main():


    pongs=pong.Pong()
    theGame=gameEngine(pongs.size,"Pong",pongs,500)

    theGame.run()

main()
