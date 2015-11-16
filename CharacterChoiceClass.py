from DragonKnightClass import *
from LightningAngelClass import *
from GhostSamuraiClass import *
from PlayerClass import *
import os
class CharChoice(object):
	def __init__(self):
		self.CharList = ["Dragon Knight = 1", "Lightning Angel = 2", "Ghost Samurai = 3"]
	
	def ChooseCharacter(self):
		print (str(self.CharList))
		CharNum = input('Choose Your Character :')
		if CharNum == "1":
			os.system("cls")
			DK = DragonKnight()
			print('Your character choice is Dragon Knight')
			return DK
		if CharNum == "2":
			os.system("cls")
			LA = LightningAngel()
			print('Your character choice is Lightning Angel')
			return LA
		if CharNum == "3":
			os.system("cls")
			GS = GhostSamurai()
			print('Your character choice is Ghost Samurai')
			return GS