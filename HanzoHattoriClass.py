from EnemyClass import *
from random import randrange

class HanzoHattori(Enemy):
	def __init__(self):
		self.MaxHP = 50000
		self.currentHP = self.MaxHP
		self.DMG = 1350
		self.GoldDropped = [500]
		self.name = 'Hanzo Hattori'
		self.EXP = randrange(300)