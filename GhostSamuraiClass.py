from PlayerClass import *
import os

class GhostSamurai(Player):
	def __init__(self):
		self.currentLevel = 1
		self.DMG = 50
		self.MagDMG = 20
		self.MaxHP = 125
		self.currentHP = self.MaxHP
		self.MaxMP = 35
		self.currentMP = self.MaxMP
		self.SamuraiArmorLevel = 0
		self.ShadowBladeLevel = 0
		self.EchoingTruthLevel = 0
		self.name = "Ghost Samurai"
		self.MaxEXP = 25
		self.currentEXP = 0
		self.skillcount = 1
		self.lives = 1
	
	def LevelUp(self, player):
		player.currentEXP -= player.MaxEXP
		player.currentLevel += 1
		player.MaxEXP += 25
		player.MaxEXP += player.currentLevel
		player.DMG += 5
		player.MagDMG += 4
		player.MaxHP += 18
		player.currentHP = player.MaxHP
		player.MaxMP += 8
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
		os.system("cls")
		pause = input("Ghost Samurai may level up a passive ability.")
		skillchoice = input("1 = Shadow Blade(DMG) 2 = Samurai Armor(HP) 3 = Echoing Truth(Magic DMG)")
		if skillchoice == 1:
			player = player.LevelShadowBlade(player)
			return player
		if skillchoice == 2:
			player = player.LevelSamuraiArmor(player)
			return player
		if skillchoice == 3:
			player = player.LevelEchoingTruth(player)
			return player
			
	def LevelShadowBlade(self, player):
		player.ShadowBladeLevel += 1
		player.DMG += 50
		if player.ShadowBladeLevel >= 40:
			player.DMG += 250
		print ("DMG = " + str(player.DMG))
		return player
	
	def LevelSamuraiArmor(self, player):
		player.SamuraiArmorLevel += 1
		player.MaxHP += 100
		if player.SamuraiArmorLevel >= 40:
			player.MaxHP += 500
		player.currentHP = player.MaxHP
		print ("HP = " + str(player.currentHP))
		return player
		
	def LevelEchoingTruth(self, player):
		player.EchoingTruthLevel += 1
		player.MagDMG += 50
		if player.EchoingTruthLevel >= 40:
			player.MagDMG += 250
		print ("Magic DMG = " + str(player.MagDMG))
		return player
			
	def EtherealBlades(self, player, enemy):
		twotimesDMG = (player.MagDMG * 2)
		enemy.currentHP -= twotimesDMG
		print (str(player.name) + " attacks " + str(enemy.name) + " for " + str(twotimesDMG) + " with ethereal blades.")
		print (str(enemy.name) + "'s health is " + str(enemy.currentHP))
		return enemy