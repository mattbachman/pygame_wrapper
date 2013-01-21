from gameEngine import *
import blockBreaker

def main():


    bb=blockBreaker.blockBreaker()
    theGame=gameEngine((800,600),"Block Breaker",bb)

    theGame.run()

main()
