from PyQt6 import QtCore, QtWidgets

from enemies import *
from towerparent import *
from menusurface import *
from gamesurface import *

TILE_SIZE = 20
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 520
FPS = 30
PATH_COORDS = [[-1,2], [0,2], [1,2], [2,2], [2,1], [2,0], [3,0], [4,0], [5,0], [5,1], [5,2], 
		[5,3], [4,3], [3,3], [3,4], [3,5], [3,6], [3,7], [2,7], [1,7], [1,8], [1,9], [1,10], 
		[1,11], [1,12], [1,13], [2,13], [3,13], [4,13], [5,13], [6,13], [7,13], [8,13], [9,13], 
		[10,13],[11,13], [12,13], [13,13], [14,13], [15,13], [16,13], [17,13], [18,13], [19,13], 
		[20,13], [21,13], [22,13], [23,13], [24,13], [25,13], [26,13], [27,13], [28,13], [29,13]]

class GameEngine(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.money = 800
		self.score = 0
		self.lives = 3

		self.setFixedSize(WINDOW_WIDTH+200,WINDOW_HEIGHT)
		self.setWindowTitle('Tower Defense')

		self.game_surface = GameSurface(self)
		self.menu_surface = MenuSurface(self)

		self.setCentralWidget(self.game_surface)

		self.timer = QtCore.QBasicTimer()
		self.timer.start(FPS, self)
		self.update()

	def mousePressEvent(self, event):
		if self.game_surface.tower_clicked or self.game_surface.tower_selected:
			self.game_surface.place_tower()

	def timerEvent(self, event):
		if event.timerId() == self.timer.timerId():
			self.game_surface.timedLoop()
			self.repaint()
		else:
			QtWidgets.QFrame.timerEvent(self, event)

	def eventFilter(self, source, event):
		if event.type() == QtCore.QEvent.Type.MouseMove:
			if event.buttons() == QtCore.Qt.MouseButton.NoButton and str(source).find("GameSurface") > 0:
				pos = event.pos()
				self.game_surface.updateMouse(pos.x(), pos.y())
				self.game_surface.clicked = True
			else:
				self.game_surface.clicked = False
				self.game_surface.repaint()
		return QtWidgets.QMainWindow.eventFilter(self, source, event)

