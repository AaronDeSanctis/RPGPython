from EnemyClass import *
from random import randrange

class RogueAngel(Enemy):
	def __init__(self):
		self.MaxHP = 425000
		self.currentHP = self.MaxHP
		self.DMG = 7500
		self.GoldDropped = [500]
		self.name = 'RogueAngel'
		self.EXP = randrange(16000)