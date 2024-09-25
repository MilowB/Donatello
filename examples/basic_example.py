import sys, os
sys.path.insert(0, os.path.abspath("donatellopyzza/"))
from game import *

import time


if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    while not game.isWon():
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
            Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
        # execute the path step by step
        for a in actions:
            result, _ = turtle.execute(a)
            time.sleep(1)