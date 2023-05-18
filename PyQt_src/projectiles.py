class Projectile(object):
	def __init__(self, tower, target):
		self.tower = tower
		self.target = target

	def dealDamage(self):
		self.target.health -= self.tower.damage