from PyQt6 import QtCore, QtGui, QtWidgets
import copy, sys, json

import gamengine
from towerparent import *
from enemies import *
from projectiles import *

class GameSurface(QtWidgets.QFrame):
	def __init__(self, engine):
		QtWidgets.QFrame.__init__(self, engine)
		self.engine = engine
		self.mouse_x = -1
		self.mouse_y = -1
		self.current_wave = 1
		self.wave_sent = False
		self.wave_in_progress = False
		self.last_wave = False
		self.clicked = False
		self.tower_selected = False
		self.tower_clicked = False
		self.extra_units = 4
		self.units_sent = 0
		self.current_tower = Tower()
		self.projectiles = []
		self.towers = []
		self.enemies = []
		self.occupied = []

		self.setStyleSheet("QWidget { background: #006400 }") 
		self.setFixedSize(gamengine.WINDOW_WIDTH, gamengine.WINDOW_HEIGHT)
		
		for coord in gamengine.PATH_COORDS:
			self.occupied.append([coord[0]*gamengine.TILE_SIZE, coord[1]*gamengine.TILE_SIZE])

	def timedLoop(self):
		self.moveEnemies()
		self.dealDamage()

	def drawGrid(self, painter):
		pen = QtGui.QPen(QtGui.QColor(25, 180, 40, 55), 2, QtCore.Qt.PenStyle.SolidLine)
		painter.setPen(pen)
		for i in range(0, 600, gamengine.TILE_SIZE):
			painter.drawLine(i, 0, i, gamengine.WINDOW_HEIGHT)
			painter.drawLine(0, i, gamengine.WINDOW_WIDTH, i)

	def moveEnemies(self):
		if len(self.towers) > 0:
			for enemy in self.enemies:
				enemy.move()

	def drawEnemies(self, painter):
		for enemy in self.enemies:
			painter.setBrush(enemy.color)
			painter.drawEllipse(enemy.getCenter(), enemy.size, enemy.size)
			if enemy.finished:
				self.engine.lives -= 1
		self.enemies[:] = [tup for tup in self.enemies if tup.finished == False]
		self.enemies[:] = [tup for tup in self.enemies if tup.isDead == False]
			
	def drawPath(self, painter):
		painter.setPen(QtCore.Qt.PenStyle.NoPen)
		painter.setBrush(QtGui.QColor(244, 164, 96, 255))
		for coord in gamengine.PATH_COORDS:
			painter.drawRect(coord[0]*gamengine.TILE_SIZE, coord[1]*gamengine.TILE_SIZE, 20, 20)

	def drawTowers(self, painter):
		color = QtGui.QColor(0, 0, 0)
		painter.setPen(color)
		
		for tower in self.towers:
			painter.setBrush(tower.color)
			painter.drawRect(tower.position_x, tower.position_y, tower.size*gamengine.TILE_SIZE, tower.size*gamengine.TILE_SIZE)
   
	def get_x(self):
		if self.mouse_x > gamengine.WINDOW_WIDTH-40 and self.current_tower.size == 2:
			return gamengine.WINDOW_WIDTH-40
		return self.mouse_x

	def get_y(self):
		if self.mouse_y > gamengine.WINDOW_HEIGHT-40 and self.current_tower.size == 2:
			return gamengine.WINDOW_HEIGHT-40
		return self.mouse_y

	def drawOutline(self, painter):
		if self.clicked:
			painter.setPen(QtCore.Qt.PenStyle.NoPen)
			painter.setBrush(self.current_tower.getColor())
			painter.drawRect(self.myround(self.get_x()), self.myround(self.get_y()), self.current_tower.size*20, self.current_tower.size*20)
			painter.setBrush(QtGui.QColor(0, 0, 0, 55))
			center = QtCore.QPoint(int(self.myround(self.get_x()) + (self.current_tower.size*20/2)), int(self.myround(self.get_y()) + self.current_tower.size*20/2))
			painter.drawEllipse(center, self.current_tower.range, self.current_tower.range)
		if not self.checkPlacement() and self.clicked:
			painter.setPen(QtCore.Qt.PenStyle.NoPen)
			painter.setBrush(QtGui.QColor(0, 0, 0, 155))
			painter.drawRect(self.myround(self.get_x()), self.myround(self.get_y()), self.current_tower.size*20, self.current_tower.size*20)

	def selectTower(self, painter, tower):
		painter.setPen(QtCore.Qt.PenStyle.NoPen)
		painter.setBrush(QtGui.QColor(0, 0, 0, 55))
		painter.drawEllipse(tower.getCenter(), tower.range, tower.range)

	def myround(self, x, base=20):
		return x - (x%base)

	def updateMouse(self, x, y):
		self.mouse_y = y
		self.mouse_x = x
		self.repaint()

	def checkPlacement(self):
		if self.current_tower.size==1:
			if [self.myround(self.get_x()),self.myround(self.get_y())] in self.occupied:
				return False
		elif self.current_tower.size==2:
			if [self.myround(self.get_x()),self.myround(self.get_y())] in self.occupied or \
				[self.myround(self.get_x()),self.myround(self.get_y())+gamengine.TILE_SIZE] in self.occupied or \
				[self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())] in self.occupied or \
				[self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())+gamengine.TILE_SIZE] in self.occupied:
				return False
		return True

	def place_tower(self):
		if self.checkPlacement() and self.tower_selected:
			self.current_tower.position_x = self.myround(self.get_x())
			self.current_tower.position_y = self.myround(self.get_y())

			if self.clicked and self.engine.money >= self.current_tower.cost:
				self.towers.append(self.current_tower)
				self.tower_selected = False
				self.tower_clicked = True
				self.engine.money -= self.current_tower.cost

				if self.current_tower.size == 1:
					self.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())])
					self.current_tower.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())])
				elif self.current_tower.size == 2:
					self.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())])
					self.occupied.append([self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())])
					self.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())+gamengine.TILE_SIZE])
					self.occupied.append([self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())+gamengine.TILE_SIZE])

					self.current_tower.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())])
					self.current_tower.occupied.append([self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())])
					self.current_tower.occupied.append([self.myround(self.get_x()),self.myround(self.get_y())+gamengine.TILE_SIZE])
					self.current_tower.occupied.append([self.myround(self.get_x())+gamengine.TILE_SIZE,self.myround(self.get_y())+gamengine.TILE_SIZE])
			else:
				self.current_tower = Tower()
				self.tower_selected = False

		elif self.clicked:
			for tower in self.towers:
				if [self.myround(self.get_x()),self.myround(self.get_y())] in tower.getOccupied():
					self.current_tower = tower
					self.tower_selected = False
					self.tower_clicked = True
					break
				else:
					self.tower_clicked = False
		self.repaint()

	def dealDamage(self):
		for projectile in self.projectiles:
			projectile.dealDamage()

	def drawProjectiles(self, painter):
		pen = QtGui.QPen(QtCore.Qt.GlobalColor.black, 1, QtCore.Qt.PenStyle.SolidLine)
		painter.setPen(pen)
		self.projectiles = []
		for tower in self.towers:
			for enemies in tower.fire(self.enemies):
				painter.drawLine(tower.getCenter(), enemies.getCenter())
				self.projectiles.append(Projectile(tower,enemies))

	def drawEnemyHP(self,painter):
		painter.setPen(QtGui.QColor(0, 34, 3))
		painter.setFont(QtGui.QFont('Arial', 6))
		for enemy in self.enemies:
			painter.drawText(enemy.getHpCoord().x(),enemy.getHpCoord().y(), str(enemy.health))
   
	
	def gameOver(self, painter):
		for i in range(len(self.enemies)):
			self.enemies.pop()
		for i in range(len(self.towers)):
			self.towers.pop()
		for i in range(len(self.occupied)):
			self.occupied.pop()

		painter.setPen(QtGui.QColor(0, 34, 3))
		painter.setFont(QtGui.QFont('Arial', 50))
		painter.drawText(95,280, "GAME OVER :(")
		self.engine.timer.stop() 

	def victory(self, painter):
		for i in range(len(self.enemies)):
			self.enemies.pop()
		for i in range(len(self.towers)):
			self.towers.pop()
		for i in range(len(self.occupied)):
			self.occupied.pop()

		painter.setPen(QtGui.QColor(0, 34, 3))
		painter.setFont(QtGui.QFont('Arial', 50))
		painter.drawText(125,280, "VICTORY!")
		self.engine.timer.stop()
  
	def waveManager(self):
		json_data=open('assets/waves.json')
		data = json.load(json_data)

		id = data["wave_"+str(self.current_wave)]["type"]
		hp = int(data["wave_"+str(self.current_wave)]["HP"])
		
		if self.wave_sent and self.wave_in_progress == False:
			if self.units_sent == 0 or len(self.enemies) == 0: 
				self.enemies.insert(0, getattr(sys.modules[__name__], id)(copy.deepcopy(gamengine.PATH_COORDS), hp))
				self.units_sent += 1
			elif self.units_sent < data["wave_"+str(self.current_wave)]["units"] + self.extra_units:
				if not len(self.enemies) == 0:
					if self.enemies[0].position_x >= data["wave_"+str(self.current_wave)]["delay"]:
						self.enemies.insert(0, getattr(sys.modules[__name__], id)(copy.deepcopy(gamengine.PATH_COORDS), hp))
						self.units_sent += 1
				if self.units_sent == data["wave_"+str(self.current_wave)]["units"]:
					self.wave_sent = False
					self.wave_in_progress = True
					try:
						id = data["wave_"+str(self.current_wave + 1)]["type"]
						self.current_wave += 1
						self.units_sent = 0
					except:
						self.last_wave = True
						self.units_sent = 0
		if self.wave_in_progress and self.enemies.__len__() == 0:
			self.wave_in_progress = False
			self.wave_sent = False
   
		json_data.close()
  
	def draw(self, painter):
		if self.engine.lives <= 0:
			self.gameOver(painter)
		elif self.last_wave and self.enemies.__len__() == 0:
			self.victory(painter)
		else:
			self.waveManager()
			self.drawGrid(painter)
			self.drawPath(painter)
			self.drawTowers(painter)
			self.drawProjectiles(painter)
			if self.tower_selected:
				self.drawOutline(painter)
			if self.tower_clicked:
				self.selectTower(painter, self.current_tower)
			self.drawEnemies(painter)
			self.drawEnemyHP(painter)
   
	def paintEvent(self, event):
		painter = QtGui.QPainter()
		painter.begin(self)
		
		self.draw(painter)
	
		painter.end()
			