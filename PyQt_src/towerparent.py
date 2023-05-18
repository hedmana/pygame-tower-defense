from PyQt6 import QtCore, QtGui
from math import sqrt

from enemies import *

class Tower(object):
	def __init__(self):
     
		self.occupied = []
		self.position_x = -100
		self.position_y = -100
		
	def enemyInRange(self, enemy):
		return int(sqrt( pow((self.getCenter().x() - enemy.getCenter().x()), 2)+ pow((self.getCenter().y() - enemy.getCenter().y()), 2) )) <= self.range

	def getColor(self):
		return self.color

	def getCenter(self):
		return QtCore.QPoint(int(self.position_x + (self.size*20/2)), int(self.position_y + self.size*20/2))

	def getOccupied(self):
		return self.occupied

	def getRange(self):
		return self.range
	
class Tower1(Tower):
	def __init__(self):
		super(Tower1, self).__init__()
		self.color = QtGui.QColor(255, 80, 100, 255)

		self.damage = 1
		self.fire_rate = 5
		self.size = 1
		self.range = 120
		self.cost = 200

	def fire(self, targets):
		new_targets = []
		for target in targets:
			if self.enemyInRange(target):
				new_targets.append(target)
		try:
			return [new_targets[len(new_targets)-1]]
		except:
			return []


class Tower2(Tower):
	def __init__(self):
		super(Tower2, self).__init__()
		self.color = QtGui.QColor(0, 200, 100, 255)

		self.damage = 2
		self.fire_rate = 1
		self.size = 2
		self.range = 200
		self.cost = 200

	def fire(self, targets):
		new_targets = []
		for target in targets:
			if self.enemyInRange(target):
				new_targets.append(target)
		try:
			return [new_targets[len(new_targets)-1], new_targets[len(new_targets)-2]]
		except:
			return []

class Tower3(Tower):
	def __init__(self):
		super(Tower3, self).__init__()
		self.color = QtGui.QColor(65, 105, 225, 255)

		self.damage = 2
		self.fire_rate = 1
		self.size = 2
		self.range = 160
		self.cost = 200

	def fire(self, targets):
		new_targets = []
		for target in targets:
			if self.enemyInRange(target):
				new_targets.append(target)
		try:
			return [new_targets[len(new_targets)-1]]
		except:
			return []