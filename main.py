#basic driver for implementation of gameEngine.py
#Matt Bachman, Jan 2013

from gameEngine import *
import blockBreaker

def main():


    bb=blockBreaker.blockBreaker()
    theGame=gameEngine((800,600),"Block Breaker",bb)

    theGame.run()

main()
