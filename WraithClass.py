from EnemyClass import *
from random import randrange

class Wraith(Enemy):
	def __init__(self):
		self.MaxHP = 150
		self.currentHP = self.MaxHP
		self.DMG = 20
		self.GoldDropped = [100, 300]
		self.name = 'Wraith'
		self.EXP = randrange(80)