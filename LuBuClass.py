from EnemyClass import *
from random import randrange

class LuBu(Enemy):
	def __init__(self):
		self.MaxHP = 250000
		self.currentHP = self.MaxHP
		self.DMG = 5000
		self.GoldDropped = [500]
		self.name = 'Lu Bu'
		self.EXP = randrange(13000)