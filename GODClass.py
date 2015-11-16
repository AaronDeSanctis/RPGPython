from EnemyClass import *
from random import randrange

class GOD(Enemy):
	def __init__(self):
		self.MaxHP = 10000000
		self.currentHP = self.MaxHP
		self.DMG = 15000
		self.GoldDropped = [500]
		self.name = 'GOD'
		self.EXP = randrange(100000)