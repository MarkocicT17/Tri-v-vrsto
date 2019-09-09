import os

class XO:
    def __init__(self):
        self.on_turn = 1
        self.game = [0,0,0,
                    0,0,0,
                    0,0,0]
        self.playing = True
        self.winning_move = -1000
        self.first_play = True
        self.print_game()


    def print_game(self):
        print(self.get_game_as_string())

    def get_game_as_string(self):
        return (self.get_simbol(self.game[0]) + " | " + self.get_simbol(self.game[1]) + " | " + self.get_simbol(self.game[2]) + "\n" +
        self.get_simbol(self.game[3]) + " | " + self.get_simbol(self.game[4]) + " | " + self.get_simbol(self.game[5]) + "\n" +
        self.get_simbol(self.game[6]) + " | " + self.get_simbol(self.game[7]) + " | " + self.get_simbol(self.game[8]) + "\n")

    def get_simbol(self, num):
        if num == 1:
            return "X"
        if num == 0:
            return "-"
        if num == -1:
            return "O"

    def stolpci(self):
        #player1
        if self.game[0] + self.game[3] + self.game[6] == 3:
            return 1
        elif self.game[1] + self.game[4] + self.game[7] == 3:
            return 2
        elif self.game[2] + self.game[5] + self.game[8] == 3:
            return 3
        #player2
        elif self.game[0] + self.game[3] + self.game[6] == -3:
            return -1
        elif self.game[1] + self.game[4] + self.game[7] == -3:
            return -2
        elif self.game[2] + self.game[5] + self.game[8] == -3:
            return -3
        else:
            return 0

    def vrstice(self):
        #player1
        if self.game[0] + self.game[1] + self.game[2] == 3:
            return 4
        elif self.game[4] + self.game[5] + self.game[3] == 3:
            return 5
        elif self.game[6] + self.game[7] + self.game[8] == 3:
            return 6
        #player2
        elif self.game[0] + self.game[1] + self.game[2] == -3:
            return -4
        elif self.game[3] + self.game[4] + self.game[5] == -3:
            return -5
        elif self.game[6] + self.game[7] + self.game[8] == -3:
            return -6
        else:
            return 0

    def diagonale(self):
        #player1
        if self.game[0] + self.game[4] + self.game[8] == 3:
            return 7
        elif self.game[6] + self.game[4] + self.game[2] == 3:
            return 8
        #player2
        elif self.game[0] + self.game[4] + self.game[8] == -3:
            return -7
        elif self.game[6] + self.game[4] + self.game[2] == -3:
            return -7
        else:
            return 0

    def play(self, field_number):
        if self.first_play:
            self.first_move = field_number + 1
            self.first_play = False
        if not self.playing: 
            return
        if self.on_turn == 1:
            if self.game[field_number] == 1 or self.game[field_number] == -1:
                print('Poteza ni možna.Ponovno izberite željeno potezo.')
            else:
                self.game[field_number] = 1
                self.on_turn = 2
        else:
            if self.game[field_number] == 1 or self.game[field_number] == -1:
                print('Poteza ni možna. Ponovno izberite željeno potezo.')
            else:
                self.game[field_number] = -1
                self.on_turn = 1
        self.print_game()
        self.check_winner()

    def check_winner(self):
        vrs = self.vrstice()
        sto = self.stolpci()
        dia = self.diagonale()

        if vrs > 0:
            self.playing = False
            print("Prvi igralec zmaga")
            self.winning_move = vrs
            
        elif vrs < 0:
            self.playing = False
            print("Drugi igralec zmaga")
            self.winning_move = vrs
    

        elif sto > 0:
            self.playing = False
            print("Prvi igralec zmaga")
            self.winning_move = sto
        
        elif sto < 0:
            self.playing = False
            print("Drugi igralec zmaga")
            self.winning_move = sto
            

        elif dia > 0:
            self.playing = False
            print("Prvi igralec zmaga")
            self.winning_move = dia
            
        elif dia < 0:
            self.playing = False
            print("Drugi igralec zmaga")

            self.winning_move = dia
            
    # file = "data.txt"

    # first_move = 0
    # first = True

    # winning_move = 0

    # playing = True
    # player = 1
    

    # winner = ""
    # if winning_move > 0:
    #     winner = p1
    # else:
    #     winner = p2
    # if not os.path.isfile(file):
    #     f = open(file, "w+")
    #     f.write("win:"+winner+"\n")
    #     f.write("first_move:"+str(first_move)+"\n")
    #     f.write("winning_move:"+str(winning_move)+"\n")
    #     f.write("player:"+p1+","+p2+"\n")
    #     f.close()
    # else:
    #     with open(file) as f2:
    #         lines = f2.readlines()
    #         f2.close()
    #     f = open(file, "w+")
    #     f.truncate(0)
    #     print(lines)
    #     f.write(lines[0][0:-1]+","+winner+"\n")
    #     f.write(lines[1][0:-1] + "," + str(first_move)+"\n")
    #     f.write(lines[2][0:-1]+ "," + str(winning_move)+"\n")
    #     f.write(lines[3][0:-1]+ ","+p1+","+p2+"\n")
    #     f.close()
    # x = input("PRESS ENTER TO CLOSE")


# p1 = input("Prvi igralec: ")  #1
# p2 = input("Drugi igralec: ") #-1
# crisscross = XO()

# while crisscross.playing:
#     print("Na potezi je igralec "+str(crisscross.on_turn))
#     vnos = int(input("Izberi polje [1-9]: "))-1
#     crisscross.play(vnos)
