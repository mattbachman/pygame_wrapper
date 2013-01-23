#basic driver for implementation of gameEngine.py
#Matt Bachman, Jan 2013

import sys
sys.path.append('../..')
from gameEngine import *
import blockBreaker

def main():


    bb=blockBreaker.blockBreaker()
    theGame=gameEngine((800,600),"Block Breaker",bb,500)

    theGame.run()

main()
