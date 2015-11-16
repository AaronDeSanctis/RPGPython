from CharacterChoiceClass import *
from ArenaSelectClass import *
import os

class Program(object):
	def __init__(self):
		os.system("cls")
		print ("Knights Of Koth - Arenas")
		print ("by Aaron DeSanctis")
		
	def StartGame(self):
		CC = CharChoice()
		player = CC.ChooseCharacter()
		ASC = ArenaSelect()
		arena = ASC.ChooseArena(player)
		while True:
			player = arena.ChooseEnemy(player)
			arena = ASC.ChooseArena(player)

user = Program()
user.StartGame()