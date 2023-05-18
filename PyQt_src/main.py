from PyQt6 import QtWidgets
import sys

from gamengine import *

APP = QtWidgets.QApplication(sys.argv)

# Runs the program by calling the game engine class
def main(): 
    game = GameEngine()
    game.show()
    APP.installEventFilter(game)
    sys.exit(APP.exec())
    
if __name__ == '__main__':
    main()