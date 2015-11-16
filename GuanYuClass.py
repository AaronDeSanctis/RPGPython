from EnemyClass import *
from random import randrange

class GuanYu(Enemy):
	def __init__(self):
		self.MaxHP = 150000
		self.currentHP = self.MaxHP
		self.DMG = 3000
		self.GoldDropped = [500]
		self.name = 'Guan Yu'
		self.EXP = randrange(10000)