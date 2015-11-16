class Player(object):
	def __init__(self):
		self.currentLevel = 0
		self.DMG = 0
		self.MagDMG = 0
		self.currentHP = 0
		self.currentMP = 0
		self.MaxHP = 0
		self.MaxMP = 0
		self.EXP = 0
		self.MaxEXP = 5
		
	def Attack(self, player, enemy):
		enemy.currentHP -= player.DMG
		print (str(player.name) + " attacks " + str(enemy.name) + " for " + str(player.DMG) + " damage.")
		print (str(enemy.name) + " has " + str(enemy.currentHP) + "HP")
		return enemy
		
	def SpendMP(self, player):
		player.currentMP -= 10
		player.currentMP -= player.currentLevel
		return player