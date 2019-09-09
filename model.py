import os
import random, json
from game import XO
class Model:

	def __init__(self):
		self.test = 0
		self.igralec1 = 'Igralec 1'
		self.igralec2 = 'Igralec 2'
		self.xo = XO()
		
	def najvec_zmag(self,lines):
		line = lines[0][4::].split(",")
		winners = dict()
		for x in line:
			if x not in winners:
				winners[x] = 1
			else:
				winners[x] = winners[x]+1
		most_wins = max(winners.values())
		winner = ""
		for name, num in winners.items():  
			if num == most_wins:
				winner = name
		return winner
		
	def najvec_igranih_iger(self,lines):
		line = lines[3][7::].split(",") 
		players = dict()
		for x in line:
			if x not in players:
				players[x] = 1
			else:
				players[x] = players[x]+1
		most_plays = max(players.values())
		player = ""
		for name, num in players.items():  
			if num == most_plays:
				player = name
		return player
	
	def najpogostejsa_prva_poteza(self,lines):
		line = lines[1][11::].split(",") 
		starts = dict()
		for x in line:
			if x not in starts:
				starts[x] = 1
			else:
				starts[x] = starts[x]+1
		most_plays = max(starts.values())
		play = ""
		for name, num in starts.items():  
			if num == most_plays:
				play = name	
				return play
	def new_game(self):
		self.xo = XO()

	def najpogostejsa_zmagovalna_poteza(self,lines):
		line = lines[2][13::].split(",") 
		ends = dict()
		for x in line:
			if abs(int(x)) not in ends:
				ends[x] = 1
			else:
				ends[x] = ends[x]+1
		most_plays = max(ends.values())
		end = ""
		for name, num in ends.items():  
			if num == most_plays:
				end = abs(int(name))
		end_move = ""
		print("END",end)
		if end == 1:
			end_move = "1,4,7"
		elif end == 2:
			end_move = "2,5,8"
		elif end == 3:
			end_move = "3,6,9"
		elif end == 4:
			end_move = "1,2,3"
		elif end == 5:
			end_move = "4,5,6"
		elif end == 6:
			end_move = "7,8,9"
		elif end == 7:
			end_move = "1,5,9"
		elif end == 8:
			end_move = "7,5,3"
		return end_move

