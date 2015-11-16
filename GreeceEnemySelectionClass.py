from RatClass import *
from WraithClass import *
from ChimeraClass import *
from SkeletonKingClass import *
from TheMightyZeusClass import *
from EnemyClass import *
from ArenaSelectClass import *
import os

class GreeceEnemySelection(object):
	def __init__(self):
		self.enemyList = ["Rat=1", "Wraith=2", "Chimera=3", "Skeleton King=4", "The Mighty Zeus=5"]
	
	def ChooseEnemy(self):
		print (str(self.enemyList))
		print (["Arena Select = 0"])
		EnemyNum = input("Choose Your Enemy : ")
		if EnemyNum == "1":
			R = Rat()
			os.system("cls")
			print('Rat!!')
			return R
		if EnemyNum == "2":
			W = Wraith()
			os.system("cls")
			print("A Wraith attacks from above!!")
			return W
		if EnemyNum == "3":
			C = Chimera()
			os.system("cls")
			print('A chained chimera is released is heading right for you!!')
			return C
		if EnemyNum == "4":
			S = SkeletonKing()
			os.system("cls")
			print("A great silence looms over you. The Skeleton King never truly dies. Defeat this BOSS!!!!")
			return S
		if EnemyNum == "5":
			T = TheMightyZeus()
			os.system("cls")
			print("Your insane. No one challenges The Mighty Zeus and lives. You have dug your own grave....")
			return T
		if EnemyNum == "0":
			os.system("cls")
			return None
		else:
			R = Rat()
			os.system("cls")
			print('Rat!!')
			return R
		
		