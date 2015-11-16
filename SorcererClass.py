from EnemyClass import *
from random import randrange

class Sorcerer(Enemy):
	def __init__(self):
		self.MaxHP = 50000
		self.currentHP = self.MaxHP
		self.DMG = 1350
		self.GoldDropped = [500]
		self.name = 'Sorcerer'
		self.EXP = randrange(4000)