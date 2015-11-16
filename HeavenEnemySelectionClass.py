from DemonClass import *
from RogueAngelClass import *
from ArchangelMichaelClass import *
from GODClass import *
from LuciferClass import *
from ArenaSelectClass import *

class HeavenEnemySelection(object):
	def __init__(self):
		self.enemyList = ["Demon=1", "Rogue Angel=2", "Archangel Michael=3", "GOD=4", "???=6"]
	
	def ChooseEnemy(self):
		print (str(self.enemyList))
		print ("Arena Select=0")
		EnemyNum = input("Choose Your Enemy : ")
		if EnemyNum == "1":
			D = Demon()
			print('A demon commanded by evil rises')
			return D
		if EnemyNum == "2":
			RA = RogueAngel()
			print("A rogue angel tries to impale you")
			return AC
		if EnemyNum == "3":
			AM = ArchangelMichael()
			print('Even the Archangel Michael has been corrupted by evil.. Defeat him or perish.')
			return AM
		if EnemyNum == "4":
			G = GOD()
			pause = input("You look up and see GOD. In all his glory.")
			pause = input("He is corrupted by Lucifer.")
			pause = input("He intends to inflict his wrath upon the living.")
			pause = input("Kill GOD NOW!!! or the human race shall perish!!!")
			return G
		if EnemyNum == "6":
			six = input("")
			if six == 6:
				six = input("")
				if six == 6:
					six = input("")
					if six == 6:
						pause = input("HAHAHAHAHAHAHAHA....")
						pause = input("You think you can DEFEAT ME??!!")
						pause = input("I AM LUCIFER!!!!")
						pause = input("Come. Look upon the heavens.")
						pause = input("I have won...")
						pause = input("I have conquered GOD once and for all.")
						pause = input("You have already lost...")
						L = Lucifer()
						return L
					else:
						D = Demon()
						print("HAHAHAHA")
						return D	
				else:
					D = Demon()
					print("HAHAHAHA")
					return D		
			else:
				D = Demon()
				print("HAHAHAHA")
				return D
				
		if EnemyNum == "0":
			return None
		else:
			D = Demon()
			return D