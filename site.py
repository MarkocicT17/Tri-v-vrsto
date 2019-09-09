import model
import os
import operator
import bottle
from bottle import route, run, Response, template, request

igra = model.Model()
shranjena_statistika = False
app = bottle.default_app()
file ='data.txt'

def get_simbol(num):
	if num == 1:
		return "X"
	if num == -1:
		return "O"
	if num == 0:
		return "-"
	
	
@bottle.post('/igraj/<num:int>/')
def igraj(num):
	igra.xo.play(num)
	return index()

@bottle.post('/igralci/')
def nastavi_igralce():
	igralec1 = request.forms.get("Igralec1")
	if(igralec1 != ''):
		igra.igralec1 = igralec1
	igralec2 = request.forms.get("Igralec2")
	if(igralec2 != ''):
		igra.igralec2 = igralec2
	return index()


@bottle.post('/novaIgra/')
def new_game():
	igra.new_game()
	return index()

def zmagovalec():
	if igra.xo.winning_move == -1000:
		return ''
	if igra.xo.winning_move >= 0:
		shrani_statistiko()
		return 'Prvi igralec'
	if igra.xo.winning_move <= 0:
		shrani_statistiko()
		return 'Drugi igralec'

def shrani_statistiko():
	if shranjena_statistika:
		return
	winner = ""
	if igra.xo.winning_move > 0:
		winner = igra.igralec1
	else:
		winner = igra.igralec2
	if not os.path.isfile(file):
		f = open(file, "w+")
		f.write("win:"+winner+"\n")
		f.write("first_move:"+str(igra.xo.first_move)+"\n")
		f.write("winning_move:"+str(igra.xo.winning_move)+"\n")
		f.write("player:"+igra.igralec1+","+igra.igralec2+"\n")
		f.close()
	else:
		with open(file) as f2:
			lines = f2.readlines()
		with open(file, "w+") as f:
			f.truncate(0)
			print(lines)
			f.write(lines[0][0:-1]+","+winner+"\n")
			f.write(lines[1][0:-1] + "," + str(igra.xo.first_move)+"\n")
			f.write(lines[2][0:-1]+ "," + str(igra.xo.winning_move)+"\n")
			f.write(lines[3][0:-1]+ ","+igra.igralec1+","+igra.igralec2+"\n")

@route('/')
def index():
	polje_1 = get_simbol(igra.xo.game[0])
	polje_2 = get_simbol(igra.xo.game[1])
	polje_3 = get_simbol(igra.xo.game[2])
	polje_4 = get_simbol(igra.xo.game[3])
	polje_5 = get_simbol(igra.xo.game[4])
	polje_6 = get_simbol(igra.xo.game[5])
	polje_7 = get_simbol(igra.xo.game[6])
	polje_8 = get_simbol(igra.xo.game[7])
	polje_9 = get_simbol(igra.xo.game[8])
	winner = ""
	if igra.xo.winning_move > 0:
		winner = igra.igralec1
	else:
		winner = igra.igralec2
	return bottle.template('site.html', most_games_played = '', most_wins = '', most_frequent_winning_move = '', most_frequent_opening_move = '', polje_1 = polje_1, polje_2 = polje_2, polje_3 = polje_3, polje_4 = polje_4, polje_5 = polje_5, polje_6 = polje_6, polje_7 = polje_7, polje_8 = polje_8, polje_9 = polje_9, zmagovalec = winner, igralec_1 = igra.igralec1, igralec_2 = igra.igralec2 )

	

@bottle.post('/izracun/')
def izracunaj():
	polje_1 = get_simbol(igra.xo.game[0])
	polje_2 = get_simbol(igra.xo.game[1])
	polje_3 = get_simbol(igra.xo.game[2])
	polje_4 = get_simbol(igra.xo.game[3])
	polje_5 = get_simbol(igra.xo.game[4])
	polje_6 = get_simbol(igra.xo.game[5])
	polje_7 = get_simbol(igra.xo.game[6])
	polje_8 = get_simbol(igra.xo.game[7])
	polje_9 = get_simbol(igra.xo.game[8])
	winner = ""
	if igra.xo.winning_move > 0:
		winner = igra.igralec1
	else:
		winner = igra.igralec2
	if not os.path.isfile(file):
		return bottle.template('site.html', most_games_played = 'Igra še ni bila igrana', most_wins = '', most_frequent_winning_move = '', most_frequent_opening_move = '', polje_1 = polje_1, polje_2 = polje_2, polje_3 = polje_3, polje_4 = polje_4, polje_5 = polje_5, polje_6 = polje_6, polje_7 = polje_7, polje_8 = polje_8, polje_9 = polje_9, zmagovalec = winner, igralec_1 = igra.igralec1, igralec_2 = igra.igralec2 )
	with open(file) as f2:
		lines = f2.readlines()
		f2.close()

#NAJVEC ZMAG		
	 #win:a,Lukas
	winner = igra.najvec_zmag(lines)
	
#NAJVEC IGRANIH IGER	
	player = igra.najvec_igranih_iger(lines)	

#NAJPOGOSTEJSA PRVA POTEZA	
	play = igra.najpogostejsa_prva_poteza(lines)

#NAJPOGOSTEJSA ZMAGOVALNA POTEZA	
	end_move = igra.najpogostejsa_zmagovalna_poteza(lines)

	return bottle.template('site.html', most_games_played = player, most_wins = winner, most_frequent_winning_move = end_move, most_frequent_opening_move = play,polje_1 = polje_1, polje_2 = polje_2, polje_3 = polje_3, polje_4 = polje_4, polje_5 = polje_5, polje_6 = polje_6, polje_7 = polje_7, polje_8 = polje_8, polje_9 = polje_9, zmagovalec = winner, igralec_1 = igra.igralec1, igralec_2 = igra.igralec2 )


bottle.run(reloader=True, debug=True)







