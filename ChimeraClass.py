from EnemyClass import *
from random import randrange

class Chimera(Enemy):
	def __init__(self):
		self.MaxHP = 350
		self.currentHP = self.MaxHP
		self.DMG = 75
		self.GoldDropped = [250, 750]
		self.name = 'Chimera'
		self.EXP = randrange(275)