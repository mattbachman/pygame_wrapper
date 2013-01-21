from gameEngine import *
import blockBreaker

def main():
    # Define some colors
##    global black = ( 0, 0, 0)
##    global white = ( 255, 255, 255)
##    global green = ( 0, 255, 0)
##    global red = ( 255, 0, 0)

    bb=blockBreaker.blockBreaker()
    theGame=gameEngine((800,600),"Block Breaker",bb)

    theGame.run()

main()
