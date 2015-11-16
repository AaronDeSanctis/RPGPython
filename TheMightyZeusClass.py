from EnemyClass import *
from random import randrange

class TheMightyZeus(Enemy):
	def __init__(self):
		self.MaxHP = 25000
		self.currentHP = self.MaxHP
		self.DMG = 750
		self.GoldDropped = [50000]
		self.name = 'The Mighty Zeus'
		self.EXP = randrange(3000)