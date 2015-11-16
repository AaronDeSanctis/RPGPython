from AncientGreeceClass import *
from FeudalJapanClass import *
from HeavenClass import *
import os

class ArenaSelect(object):
	def __init__(self):
		self.arenaList = ["Ancient Greece = 1 (Easy)", "Feudal Japan = 2 (Hard)", "Heaven = 3 (Insane)"]
		
	def ChooseArena(self, player):
		print (str(self.arenaList))
		ArenaNum = input("Choose Your Arena : ")
		if ArenaNum == "1":
			os.system("cls")
			arena = AncientGreece(player)
			print(str(player.name) + ' has entered Ancient Greece')
			return arena
		if ArenaNum == "2":
			os.system("cls")
			arena = FeudalJapan(player)
			print(str(player.name) + ' has entered Feudal Japan')
			return arena
		if ArenaNum == "3":
			os.system("cls")
			arena = Heaven(player)
			print(str(player.name) + ' has entered the gates of Heaven')
			return arena
		else:
			self.ChooseArena()