from SorcererClass import *
from NinjaClass import *
from PangDeClass import *
from GuanYuClass import *
from LuBuClass import *
from ArenaSelectClass import *
from EnemyClass import *

class JapanEnemySelection(object):
	def __init__(self):
		self.enemyList = ["Sorcerer=1", "Ninja=2", "Pang De=3", "Guan Yu=4", "Lu Bu=5"]
	
	def ChooseEnemy(self):
		print (str(self.enemyList))
		print ("Arena Select=0")
		EnemyNum = input("Choose Your Enemy : ")
		if EnemyNum == "1":
			S = Sorcerer()
			print('A sorcerer appears behind you!')
			return S
		if EnemyNum == "2":
			N = Ninja()
			print("A ninja exits the shadows..")
			return N
		if EnemyNum == "3":
			P = PangDe()
			print('I am Pang De! My halbreds will taste your flesh!!')
			return P
		if EnemyNum == "4":
			G = GuanYu()
			print("The horselord Guan Yu charges in your direction. You brace for battle.")
			return G
		if EnemyNum == "5":
			L = LuBu()
			print("The legendary Lu Bu has come to finish you off.")
			return L
		if EnemyNum == "0":
			return None
		else:
			S = Sorcerer()
			print('A sorcerer appears behind you!')
			return S
			