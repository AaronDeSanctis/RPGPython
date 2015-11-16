from EnemyClass import *
from random import randrange

class Ninja(Enemy):
	def __init__(self):
		self.MaxHP = 75000
		self.currentHP = self.MaxHP
		self.DMG = 1500
		self.GoldDropped = [500]
		self.name = 'Ninja'
		self.EXP = randrange(6000)