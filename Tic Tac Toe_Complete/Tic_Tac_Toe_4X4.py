from time import *

class player:

    def __init__(self,name,character):
        self.name = name
        self.character = character

    @staticmethod
    def board():
        print("      0     1     2     3")
        print()
        print("         |     |     |")
        for row, i in enumerate(game):
            print(row, "  __%s__|__%s__|__%s__|__%s__"%(i[0],i[1],i[2],i[3]),end="")
            print("\n         |     |     |")

    def move(self,z,j):
        try:
            term = []
            for i in z:
                term.append(int(i))
            if game[term[0]][term[1]]=='-':
                game[term[0]][term[1]] = j
                player.board()
                player.main(self)
            else:
                print("\nThis Position Is Already Filled, you lost your chance")
        except Exception as e:
            sleep(1)
            print("\nYou lost your chance, ",e)
            player.board()
            print()


    def winning(row):
        if row.count(row[0]) == len(row) and row[0] != '-':
            print("Game won!")
            return True
    #OR
    def winning1(row):
        if row[0]!='-':
            counting = 0
            for i in row:
                if i==row[0]:
                    counting+=1
            if counting==len(row):
                print("Game won!")
                return True

    def horizontal_win(self):
        for row in game:
            if player.winning(row):
                print("Game won! - Horizontally by Player - ",self.name,"which have ",self.character)
                return True
        return False

    def vertical_win(self):
        check = []
        for i in range(len(game)):
            for row in game:
                check.append(row[0])
            if player.winning(check):
                print("Game won! - Vertically by Player - ",self.name,"which have ",self.character)
                return True
        return False

    def diagonal_win(self):
        check = []
        for i, row in enumerate(game):
            check.append(row[i])

        check1 = []
        x = 4
        for row in game:
            x-=1
            check1.append(row[x])

        if player.winning(check) or player.winning(check1):
            print("Game won! - Diagonally By Player ",self.name,"which have ",self.character)
            return True
        return False

    @staticmethod
    def main(self):
        global sipping
        if player.horizontal_win(self) or player.vertical_win(self) or player.diagonal_win(self):
            sipping = True



game = [['-'] * 4 for _ in range(4)]

x = player(1,'O')
y = player(2,'X')
print("Let's play Tic Tac Toe\nIt's gonna be a two player game\n")
sleep(3)
print("First Player will be assigned 'O'\nSecond player will be 'X'\n")
sleep(4)
player.board()
print('This will be the board we are gonna play, ROW is ---<horizonaatal> and COLUMN is | <vertical>\n')
print('For example, to row - "0" and column - "1" should be writtern as 01\n')
sleep(2)
var = 1
sipping = False
while not sipping :
    sleep(1)
    var = 1-var
    if var==0:
        z = input("Enter Your move , player 1, first row than column btwn [0-2] - ")
        x.move(z,'O')
    else:
        z = input("Enter Your move , player 2, first row than column btwn [0-2] - ")
        y.move(z,'X')
