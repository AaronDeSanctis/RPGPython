from EnemyClass import *
from random import randrange

class Lucifer(Enemy):
	def __init__(self):
		self.MaxHP = 150000000
		self.currentHP = self.MaxHP
		self.DMG = 50000
		self.GoldDropped = [500]
		self.name = 'Lucifer'
		self.EXP = randrange(1500000)