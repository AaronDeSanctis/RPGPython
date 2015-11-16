from EnemyClass import *
from random import randrange

class Rat(Enemy):
	def __init__(self):
		self.MaxHP = 75
		self.currentHP = self.MaxHP
		self.DMG = 8
		self.GoldDropped = [50,150]
		self.name = 'Rat'
		self.EXP = randrange(25)
		