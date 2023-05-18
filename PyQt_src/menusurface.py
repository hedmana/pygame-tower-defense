from PyQt6 import QtGui, QtWidgets

import gamengine
from towerparent import *


class MenuSurface(QtWidgets.QFrame):
	def __init__(self, engine):
		QtWidgets.QFrame.__init__(self, engine)
		self.game_surface = engine.game_surface
		self.engine = engine
		self.isPaused = False
  
		self.setStyleSheet("QWidget { background: #ADD8E6 }") 
		self.setGeometry(gamengine.WINDOW_WIDTH, 0, 200, gamengine.WINDOW_HEIGHT)

		y_diff = 85
		tower1 = QtWidgets.QPushButton("Tower 1", self)
		tower1.move(10, y_diff)

		tower2 = QtWidgets.QPushButton("Tower 2", self)
		tower2.move(110, y_diff)

		tower3 = QtWidgets.QPushButton("Tower 3", self)
		tower3.move(60, y_diff+30)

		tower1.clicked.connect(self.tower1)
		tower2.clicked.connect(self.tower2)
		tower3.clicked.connect(self.tower3)
		self.pauseButton()
		self.nextWaveButton()

	def towerSelected(self):
		self.game_surface.tower_selected = True
		self.game_surface.tower_clicked = False
		
	def tower1(self):
		self.towerSelected()
		self.game_surface.current_tower = Tower1()

	def tower2(self):
		self.towerSelected()
		self.game_surface.current_tower = Tower2()

	def tower3(self):
		self.towerSelected()
		self.game_surface.current_tower = Tower3()

	def pauseButton(self):
		self.pauseButton = QtWidgets.QPushButton("Pause", self)
		self.pauseButton.move(110, 480)
		self.pauseButton.clicked.connect(self.pauseGame) 

	def pauseGame(self):
		if self.isPaused == False:
			self.pauseButton.setText('Play')
			self.isPaused = True 
			self.engine.timer.stop()  
		else:
			self.pauseButton.setText('Pause')
			self.isPaused = False 
			self.engine.timer.start(gamengine.FPS, self.engine)  

	def nextWaveButton(self):
		self.nextWave = QtWidgets.QPushButton("Next Wave", self)
		self.nextWave.move(15, 480)
		self.nextWave.clicked.connect(self.nextWaveAction) 

	def nextWaveAction(self):
		self.game_surface.wave_sent = True
	
	def draw(self, painter):
		y_diff =5
		painter.setPen(QtGui.QColor(0, 0, 0))
		painter.setBrush(QtGui.QColor(0, 0, 0, 0))
		painter.drawRect(10, y_diff, 180, y_diff + 70)
		painter.setPen(QtGui.QColor(0, 34, 3))
		painter.setFont(QtGui.QFont('Arial', 10))
		painter.drawText(15,20, "MONEY: "+ str(self.engine.money))
		painter.drawText(15,40, "LIVES: "+ str(self.engine.lives))
		painter.drawText(15,60, "WAVE: "+ str(self.game_surface.current_wave - 1)+" / 3")
  
		y_diff = 150
		painter.setPen(QtGui.QColor(0, 0, 0))
		painter.setBrush(QtGui.QColor(0, 0, 0, 0))
		painter.drawRect(10, y_diff, 180, 80)

		if self.game_surface.tower_clicked or self.game_surface.tower_selected:
			painter.setPen(QtGui.QColor(0, 34, 3))
			painter.setFont(QtGui.QFont('Arial', 10))
			painter.drawText(15,y_diff+15, "Damage: " + str(self.game_surface.current_tower.damage))
			painter.drawText(15,y_diff+35, "Range: " + str(self.game_surface.current_tower.range))
			painter.drawText(15,y_diff+55, "Fire rate: " + str(self.game_surface.current_tower.fire_rate))
  
	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
  
		self.draw(painter)

		painter.end()
