from EnemyClass import *
from random import randrange

class ArchangelMichael(Enemy):
	def __init__(self):
		self.MaxHP = 600000
		self.currentHP = self.MaxHP
		self.DMG = 9000
		self.GoldDropped = [500]
		self.name = 'Archangel Michael'
		self.EXP = randrange(20000)