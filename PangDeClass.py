from EnemyClass import *
from random import randrange

class PangDe(Enemy):
	def __init__(self):
		self.MaxHP = 100000
		self.currentHP = self.MaxHP
		self.DMG = 2000
		self.GoldDropped = [500]
		self.name = 'Pang De'
		self.EXP = randrange(7500)