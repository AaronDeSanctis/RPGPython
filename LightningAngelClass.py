from PlayerClass import *
import os

class LightningAngel(Player):
	def __init__(self):
		self.currentLevel = 1
		self.DMG = 20
		self.MagDMG = 50
		self.MaxHP = 110
		self.currentHP = self.MaxHP
		self.MaxMP = 50
		self.currentMP = self.MaxMP
		self.DivineAegisLevel = 0
		self.HolyLanceLevel = 0
		self.ThunderGemLevel = 0
		self.name = "Lightning Angel"
		self.MaxEXP = 25
		self.currentEXP = 0
		self.skillcount = 4
		self.lives = 1
	
	def LevelUp(self, player):
		player.currentEXP -= player.MaxEXP
		player.currentLevel += 1
		player.MaxEXP += 25
		player.MaxEXP += player.currentLevel
		player.DMG += 4
		player.MagDMG += 5
		player.MaxHP += 15
		player.currentHP = player.MaxHP
		player.MaxMP += 11
		player.currentMP = player.MaxMP
		player.skillcount += 1
		print (str(player.name) + " has leveled up!!!!")
		print (str(player.name) + " has leveled to " + str(player.currentLevel) + "") 
		print (str(player.name) + "'s HP = " + str(player.currentHP))
		print (str(player.name) + "'s DMG = " + str(player.DMG))
		print (str(player.name) + "'s MP = " + str(player.currentMP))
		print (str(player.name) + "'s Magic DMG = " + str(player.MagDMG))
		if player.skillcount == 5:
			player.skillcount = 0
			player = player.SkillLevelUp(player)
		if player.currentEXP >= player.MaxEXP:
			player = player.LevelUp(player)
		return player
			
	def SkillLevelUp(self, player):
		pause = input("Lightning Angel may level up a passive ability.")
		skillchoice = input("1 = Holy Lance(DMG) 2 = Divine Aegis(HP) 3 = Thunder Gem(Magic DMG)")
		if skillchoice == 1:
			player = player.LevelHolyLance(player)
			return player
		if skillchoice == 2:
			player = player.LevelDivineAegis(player)
			return player
		if skillchoice == 3:
			player = player.LevelThunderGem(player)
			return player

				
	def LevelThunderGem(self, player):
		player.ThunderGemLevel += 1
		player.MagDMG += 50
		if player.ThunderGemLevel >= 40:
			player.MagDMG += 250
		print ("Magic DMG = " + str(player.MagDMG))
		return player

	def LevelDivineAegis(self, player):
		player.DivineAegisLevel += 1
		player.MaxHP += 100
		if player.DivineAegisLevel >= 40:
			player.MaxHP += 500
		player.currentHP = player.MaxHP
		print ("HP = " + str(player.currentHP))
		return player
			
	def LevelHolyLance(self, player):
		player.HolyLanceLevel += 1
		player.DMG += 50
		if player.HolyLanceLevel >= 40:
			player.DMG += 250
		print ("DMG = " + str(player.DMG))
		return player
		
	def ChainLightning(self, player, enemy):
		twotimesDMG = (player.MagDMG * 2)
		enemy.currentHP -= twotimesDMG
		print (str(player.name) + " attacks " + str(enemy.name) + " for " + str(twotimesDMG) + " with Chain Lightning.")
		print (str(enemy.name) + "'s health is " + str(enemy.currentHP))
		return enemy