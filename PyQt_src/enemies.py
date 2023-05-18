from PyQt6 import QtCore, QtGui
from math import floor

class Enemy(object):
	def __init__(self, ep=None):
		
		self.enemyPath = ep

		self.size = 8
		self.finished = False
		self.isDead = False

		self.position_x = self.enemyPath[0][0]*20
		self.position_y = self.enemyPath[0][1]*20
		self.totalDistance = 0

		self.current_block = [self.enemyPath[0][0],self.enemyPath[0][1]]
		self.direction = "R"

	
	def getCenter(self):
		return QtCore.QPoint(self.position_x+10, self.position_y+10)

	def getHpCoord(self):
		return QtCore.QPoint(self.position_x-10, self.position_y)

	def checkHp(self):
		if self.health <= 0:
			self.isDead = True 

	def getCurrentBlock(self):
		if self.direction == "U":
			current_y = int(floor((self.position_y+20)/20))
			if self.position_y <= 0:
				current_y = 0
		else:
			current_y = int(floor(self.position_y/20))
			if current_y <= 0:
				current_y = 0

		if self.direction == "L":
			current_x = int(floor((self.position_x+18)/20))
		else:
			current_x = int(floor(self.position_x/20))
		return [current_x, current_y]

	def getNextBlock(self):
		if self.direction	== "R":
			return [self.getCurrentBlock()[0]+1,self.getCurrentBlock()[1]]
		elif self.direction	== "L":
			return [self.getCurrentBlock()[0]-1,self.getCurrentBlock()[1]]
		elif self.direction	== "U":
			return [self.getCurrentBlock()[0],self.getCurrentBlock()[1]-1]
		elif self.direction	== "D":
			return [self.getCurrentBlock()[0],self.getCurrentBlock()[1]+1]
		return None

	def move(self):
		temp = self.current_block
		self.current_block = self.getCurrentBlock()

		if temp != self.current_block:
			try:
				self.enemyPath.pop(0)
				if self.enemyPath[1] != self.getNextBlock():
					if self.getCurrentBlock()[1] < self.enemyPath[1][1]:
						self.direction = "D"
					elif self.getCurrentBlock()[1] > self.enemyPath[1][1]:
						self.direction = "U"
					elif self.getCurrentBlock()[0] < self.enemyPath[1][0]:
						self.direction = "R"
					elif self.getCurrentBlock()[0] > self.enemyPath[1][0]:
						self.direction = "L"
			except:
				self.finished = True 
		if self.direction == "R":
			self.position_x += self.speed
		elif self.direction == "D":
			self.position_y += self.speed
		elif self.direction == "L":
			self.position_x -= self.speed
		elif self.direction == "U":
			self.position_y -= self.speed

		self.totalDistance += self.speed

		self.checkHp()

class Type1(Enemy):
	def __init__(self, ep=None, HP=100):
		super(Type1, self).__init__(ep)
		self.health = HP
		self.speed = 2
		self.color = QtGui.QColor(25, 80, 100, 255)

class Type2(Enemy):
	def __init__(self, ep=None, HP=100):
		super(Type2, self).__init__(ep)
		self.health = HP
		self.speed = 2
		self.color = QtGui.QColor(25, 180, 10, 255)

class Type3(Enemy):
	def __init__(self, ep=None, HP=100):
		super(Type3, self).__init__(ep)
		self.health = HP
		self.speed = 2
		self.color = QtGui.QColor(25, 180, 10, 255)
		
		
		

