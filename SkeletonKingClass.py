from EnemyClass import *
from random import randrange

class SkeletonKing(Enemy):
	def __init__(self):
		self.MaxHP = 5000
		self.currentHP = self.MaxHP
		self.DMG = 300
		self.GoldDropped = [10000]
		self.name = 'Skeleton King'
		self.EXP = randrange(400)