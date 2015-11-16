from HeavenEnemySelectionClass import *
from DemonClass import *
from RogueAngelClass import *
from ArchangelMichaelClass import *
from GODClass import *
from LuciferClass import *
from GhostSamuraiClass import *
from LightningAngelClass import *
from DragonKnightClass import *
import os

class Heaven(object):
	def __init__(self, player):
		self.player = player
		self.playerAlive = True
		self.enemyAlive = True
		self.playerTurn = True
		self.EnemyTurn = False
		self.Turn = 0
		self.attack = 0
		self.GSOptions = ['1 = Physical Attack', '2 = Ethereal Blades']
		self.LAOptions = ['1 = Physical Attack', '2 = Chain Lightning']
		self.DKOptions = ['1 = Physical Attack', '2 = Implosion']
		
	def ChooseEnemy(self, player):
		HES = HeavenEnemySelection()
		enemy = HES.ChooseEnemy()
		if enemy == None:
			return player
		else:
			player = self.BattleEnemy(player, enemy)
			return player
		
	def BattleEnemy(self, player, enemy):
		while (self.enemyAlive == True or self.playerAlive == True):
			try:
				enemy = self.AttackOptions(player, enemy)
				if enemy.currentHP <= 0:
					os.system("cls")
					print (str(player.name) + " has killed the " + (str(enemy.name)) + ".")
					player = enemy.DropEXP(player, enemy)
					self.playerAlive = False
					player = self.ChooseEnemy(player)
					return player
				player = enemy.Attack(player, enemy)	
				if player.currentHP <= 0:
					os.system("cls")
					print (str(player.name) + "has died.")
					if player.lives <= 0:
						print("Game Over")
						player.currentHP = 0
					if player.lives == 1:
						player.lives -= 1
						player.currentHP = player.MaxHP
						pause = input(str(player.name) + " is out of lives!!")
						player = self.ChooseEnemy(player)
						self.playerAlive = False
						return player
			except:
				print ("HP = "  + str(player.currentHP))
				return player
				
						
	def AttackOptions(self, player, enemy):
		DK = DragonKnight()
		GS = GhostSamurai()
		LA = LightningAngel()
		if type(player) == type(GS):
			print (str(self.GSOptions))
			attackGS = input('Choose Your Attack : ')
			if attackGS == "1":
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy
			if attackGS == "2":
				os.system("cls")
				player = player.SpendMP(player)
				if player.currentMP < 0:
					print(str(player.name) + " is out of MP. So " + str(player.name) + " attacks instead.")
					enemy = player.Attack(player, enemy)
					return enemy
				else:
					enemy = player.EtherealBlades(player, enemy)	
					return enemy
			else:
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy
		if type(player) == type(LA):
			print (str(self.LAOptions))
			attackLA = input('Choose Your Attack : ')
			if attackLA == "1":
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy
			if attackLA == "2":
				os.system("cls")
				player = player.SpendMP(player)
				if player.currentMP < 0:
					print(str(player.name) + " is out of MP. So " + str(player.name) + " attacks instead.")
					enemy = player.Attack(player, enemy)
					return enemy
				else:
					enemy = player.ChainLightning(player, enemy)
					return enemy
			else:
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy
		if type(player) == type(DK):
			print (str(self.DKOptions))
			attackDK = input('Choose Your Attack : ')
			if attackDK == "1":
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy
			if attackDK == "2":
				os.system("cls")
				player = player.SpendMP(player)
				if player.currentMP < 0:
					print(str(player.name) + " is out of MP. So " + str(player.name) + " attacks instead.")
					enemy = player.Attack(player, enemy)
					return enemy
				else:
					enemy = player.Implosion(player, enemy)	
					return enemy		
			else:
				os.system("cls")
				enemy = player.Attack(player, enemy)
				return enemy