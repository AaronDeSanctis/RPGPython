from PlayerClass import *
import os

class DragonKnight(Player):
	def __init__(self):
		self.currentLevel = 1
		self.DMG = 60
		self.MagDMG = 10
		self.MaxHP = 150
		self.currentHP = self.MaxHP
		self.MaxMP = 10
		self.currentMP = self.MaxMP
		self.FrostArmorLevel = 0
		self.FlamingSwordLevel = 0
		self.BornOfBahamutLevel = 0
		self.name = "Dragon Knight"
		self.MaxEXP = 25
		self.currentEXP = 0
		self.skillcount = 1
		self.lives = 1
		
	def LevelUp(self, player):
		player.currentEXP -= player.MaxEXP
		player.currentLevel += 1
		player.MaxEXP += 25
		player.MaxEXP += player.currentLevel
		player.DMG += 6
		player.MagDMG += 3
		player.MaxHP += 20
		player.currentHP = player.MaxHP
		player.MaxMP += 5
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
		pause = input("Dragon Knight may level up a passive ability.")
		skillchoice = input("1 = Flaming Sword(DMG) 2 = Frost Armor(HP) 3 = Born Of Bahamut(Magic DMG)")
		if skillchoice == 1:
			player = player.LevelFlamingSword(player)
			return player
		if skillchoice == 2:
			player = player.LevelFrostArmor(player)
			return player
		if skillchoice == 3:
			player = player.LevelBornOfBahamut(player)
			return player

	def LevelFrostArmor(self, player):
		player.FrostArmorLevel += 1
		player.MaxHP += 100
		if player.FrostArmorLevel >= 40:
			player.MaxHP += 500
		player.currentHP = player.MaxHP
		print ("HP = " + str(player.currentHP))
		return player
		
	def LevelBornOfBahamut(self, player):
		player.BornOfBahamutLevel += 1
		player.MagDMG += 50
		if player.BornOfBahamutLevel >= 40:
			player.MagDMG += 250
		print ("Magic DMG = " + str(player.MagDMG))
		return player
	
	def LevelFlamingSword(self, player):
		player.FlamingSwordLevel += 1
		player.DMG += 50
		if player.FlamingSwordLevel >= 40:
			player.DMG += 250
		print ("DMG = " + str(player.DMG))
		return player

	def Implosion(self, player, enemy):
		twotimesDMG = (player.MagDMG * 2)
		enemy.currentHP -= twotimesDMG
		print (str(player.name) + " attacks " + str(enemy.name) + " for " + str(twotimesDMG) + " with an Implosion")
		print (str(enemy.name) + "'s health is " + str(enemy.currentHP))
		return enemy