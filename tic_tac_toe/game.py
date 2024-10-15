import random
import os
import time

def make_board():
    dimensions = []
    for i in range(0, 3):
        for j in range(0, 3):
            dimensions.append(position(i, j))
    return dimensions


class player:
    def __init__(self, name, symbol='?'):
        self.name = name
        self.symbol = symbol
    def print_name(self):
        return self.name


class position:
    def __init__(self, row, column, element='?'):
        self.row = row
        self.column = column
        self.element = element


class game:
    dimensions = make_board()
    played = []
    current_player = 0

    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player

    def check_board(self):
        check = []
        for i in range(0, 7, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == self.first_player.symbol)
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == self.second_player.symbol)


        for i in range(0, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == self.first_player.symbol)
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == self.second_player.symbol)

        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == self.first_player.symbol)
        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == self.second_player.symbol)

        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == self.first_player.symbol)
        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == self.second_player.symbol)

        for i in check:
            if i == True:
                return True
            
        return False
    
    def change_element(self, row, column, element):
        for i in game.dimensions:
            if i.row == row and i.column == column:
                i.element = element
        game.played.append((row, column))

    def get_dimensions(self):
        for i in game.dimensions:
            print(i.row, i.column, i.element)
    
    def allow_move(self, row, column):
        if row > 8 or row < 0 or column > 8 or column < 0:
            raise ValueError ("The given cooridinates are out of the game's dimension\nPlease choose a value between 0 and 8")
        
        if (row, column) in game.played:
            return False
        else:
            return True
        

    def draw_board(self):
        print(str(game.dimensions[0].element) + " | " + str(game.dimensions[1].element) + " | " + str(game.dimensions[2].element))
        print("_" + "_|_" + "_" + "_|_" + "_")
        print(" " + " | " + " " + " | " + " ")
        print(str(game.dimensions[3].element) + " | " + str(game.dimensions[4].element) + " | " + str(game.dimensions[5].element))
        print("_" + "_|_" + "_" + "_|_" + "_")
        print(str(game.dimensions[6].element) + " | " + str(game.dimensions[7].element) + " | " + str(game.dimensions[8].element))
        print(" " + " | " + " " + " | " + " "+"\n")




def tic_tac_toe(player1_name, player2_name):
    GREEN = "\033[0;32m" 
    CYAN = "\033[0;35m"
    YELLOW = "\033[0;33m"

    player1 = player(player1_name)
    player2 = player(player2_name)
    players = random.sample([player1, player2], 2)
    players[0].symbol = GREEN + "X" + "\033[0m"
    players[1].symbol = CYAN + "O" + "\033[0m"

    match = game(player1, player2)
    os.system("clear") 
    print("------------------------------------------")
    print("---------------Tic Tac Toe----------------")
    print("------------------------------------------")
    time.sleep(1)
    print("{} and {}, welcome to the game".format(player1.name, player2.name))
    time.sleep(1)
    print("Please wait until the game is launched..\n")
    time.sleep(2)

    while (match.check_board() == False) and (len(match.played) != 9):
        
        print("{} it's your turn\nYour symbol is: {}".format(YELLOW + players[0].name + "\033[0m", players[0].symbol))
        x = input("Enter the number of row:")
        y = input("Enter the number of column:")

        if x == 'q' or y == 'q':
            break

        x = int(x)
        y = int(y)
        if match.allow_move(x, y):
            match.change_element(x, y, players[0].symbol)
            os.system('clear')
            match.draw_board()
            possible_winner = players[0]
            players = players[::-1]
            
        else:
            print("The position you are trying to play is already fulfilled, try another move !!")
            continue

    if match.check_board() == False and len((match.played) == 9):
        print("Draw")

    elif match.check_board() == True:
        print(f"{possible_winner.name} you won the game")



if __name__=="__main__":
    tic_tac_toe("Mustafa", "Phil")

    
