from EnemyClass import *
from random import randrange

class Demon(Enemy):
	def __init__(self):
		self.MaxHP = 350000
		self.currentHP = self.MaxHP
		self.DMG = 6000
		self.GoldDropped = [500]
		self.name = 'Demon'
		self.EXP = randrange(15000)