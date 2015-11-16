class Enemy(object):
	def __init__(self):
		self.MaxHP = 0
		self.currentHp = self.MaxHP
		self.DMG = 0
		self.WeaponDropped = False
		self.GoldDropped = []
	
	def Attack(self, player, enemy):
		player.currentHP -= enemy.DMG
		print (str(enemy.name) + " attacks " + str(player.name) + " for " + str(enemy.DMG) + " damage.")
		print (str(player.name) + "'s HP is " + str(player.currentHP))
		return player
		
	def DropEXP(self, player, enemy):
		player.currentEXP += enemy.EXP
		print (str(player.name) + " has gained " + str(enemy.EXP) + " EXP from " + str(enemy.name))
		if player.currentEXP >= player.MaxEXP:
			player = player.LevelUp(player)
			return player
		else:
			return player
	
	