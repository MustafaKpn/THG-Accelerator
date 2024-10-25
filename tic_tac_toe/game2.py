import random
import sys
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

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def check_board(self):
        check = []
        for i in range(0, 7, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == self.player1.symbol)
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == self.player2.symbol)


        for i in range(0, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == self.player1.symbol)
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == self.player2.symbol)

        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == self.player1.symbol)
        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == self.player2.symbol)

        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == self.player1.symbol)
        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == self.player2.symbol)

        for i in check:
            if i:
                return True
            
        return False
    
    def change_element(self, row, column, element):
        for i in game.dimensions:
            if i.row == row and i.column == column and (row, column) not in game.played:
                i.element = element
        game.played.append((row, column))
        return (row, column)

    def get_dimensions(self):
        coordinates = []
        for i in game.dimensions:
            coordinates.append((i.row, i.column))
        return coordinates
    
    def allow_move(self, row, column):
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
    
    def game_intro(self):
        os.system("clear") 
        print("--------------------------------------------")
        print("--------------- Tic Tac Toe ----------------")
        print("--------------------------------------------")
        time.sleep(1)
        print("Welcome to the game..")
        time.sleep(1)
        print("{} VS {}".format(self.player1.name, self.player2.name))
        time.sleep(1)
        print("Please wait until the game is launched..\n")
        time.sleep(2)

    def solve_for_weights(self):
        GREEN = "\033[0;32m" 
        CYAN = "\033[0;35m"

        enemy_symbol = GREEN + "X" + "\033[0m"
        my_symbol = CYAN + "O" + "\033[0m"
        weights = {(0,0):0, (0,1):0, (0,2):0, (1,0):0, (1,1):0, (1,2):0, (2,0):0, (2,1):0}
        
        for i in game.dimensions:
            for k in [0, 1, 2]:
                if i.row == k and i.element == enemy_symbol:
                    weights[(0, k)] += 3
                if i.column == k and i.element == enemy_symbol:
                    weights[(1, k)] += 3
                if i.row == k and i.element == my_symbol:
                    weights[(0, k)] +=4
                if i.column == k and i.element == my_symbol:
                    weights[(1, k)] +=4


        for i in game.dimensions:
            for k in [0, 1, 2]:
                if i.column == k and i.row == k and i.element == enemy_symbol:
                    weights[(2,0)] += 3
                if i.column == k and i.row == k and i.element == my_symbol:
                    weights[(2,0)] += 4
            
            if i.column == 2 and i.row == 0 and i.element == enemy_symbol:
                weights[(2,1)] += 3
            if i.column == 2 and i.row == 0 and i.element == my_symbol:
                weights[(2,1)] += 4

            if i.column == 1 and i.row == 1 and i.element == enemy_symbol:
                weights[(2,1)] += 3
            if i.column == 1 and i.row == 1 and i.element == my_symbol:
                weights[(2,1)] += 4

            if i.column == 0 and i.row == 2 and i.element == enemy_symbol:
                weights[(2,1)] += 3
            if i.column == 0 and i.row == 2 and i.element == my_symbol:
                weights[(2,1)] += 4

        target = False
        for k, v in weights.items():
            if v == 6 or v == 8:
                target = k

        if not target:
            for k, v in weights.items():
                if v == 4 or v == 3:
                    target = k

        try:
            if target[0] == 0:
                for index, value in enumerate(game.dimensions):
                    if value.row == target[1] and value.element == '?':
                        self.change_element(value.row, value.column, my_symbol)
                        break


            elif target[0] == 1:
                for index, value in enumerate(game.dimensions):
                    if value.column == target[1] and value.element == '?':
                        self.change_element(value.row, value.column, my_symbol)        
                        break
            elif target[0] == 2:
                if target[1] == 0:
                    for index, value in enumerate(game.dimensions):
                        if value.row == 0 and value.column == 0 and value.element == '?':
                            self.change_element(value.row, value.column, my_symbol)
                            break
                        if value.row == 1 and value.column == 1 and value.element == '?':
                            self.change_element(value.row, value.column, my_symbol)
                            break
                        if value.row == 2 and value.column == 2 and value.element == '?':
                            self.change_element(value.row, value.column, my_symbol)
                            break
                else:
                    for index, value in enumerate(game.dimensions):
                        if value.row == 0 and value.column == 2 and value.element == '?':
                            self.change_element(0, 2, my_symbol)
                            break
                        
                        elif value.row == 1 and value.column == 1 and value.element == '?':
                            self.change_element(1, 1, my_symbol)
                            break
                        
                        elif value.row == 2 and value.column == 0 and value.element == '?':
                            self.change_element(2, 0, my_symbol)
                            break


        except TypeError:
            for i in game.dimensions:
                if (i.row, i.column) not in game.played:
                    self.change_element(i.row, i.column, my_symbol)
                    


def tic_tac_toe(player1_name, player2_name):
    GREEN = "\033[0;32m" 
    CYAN = "\033[0;35m"
    YELLOW = "\033[0;33m"
    RED = "\033[31m"

    player1 = player(player1_name)
    player2 = player(player2_name)
    players = random.sample([player1, player2], 2)
    player1.symbol = GREEN + "X" + "\033[0m"
    player2.symbol = CYAN + "O" + "\033[0m"

    match = game(player1, player2)
    match.game_intro()

    while (match.check_board() == False) and (len(match.played) != 9):
        
        if players[0].name.lower() == 'computer':
            print("It is the machine's turn")
            time.sleep(1)
            print("Picking a move..")
            time.sleep(2)
            random_move = random.choice(match.get_dimensions())
            while random_move in match.played:
                random_move = random.choice(match.get_dimensions())
            print("The random machine decided to play row:{}, column:{}".format(random_move[0], random_move[1]))
            time.sleep(3)
            match.change_element(random_move[0], random_move[1], players[0].symbol)
            os.system('clear')
            match.draw_board()
            possible_winner = players[0]
            players = players[::-1]

        elif players[0].name.lower() == 'ai':
                if len(match.played) == 0:
                    match.change_element(random.choice([0, 1, 2]), random.choice([0, 1, 2]), players[0].symbol)
                else:
                    match.solve_for_weights()
                        
                os.system('clear')
                match.draw_board()
                possible_winner = players[0]
                players = players[::-1]

        else:
            print("\n{} it's your turn\nYour symbol is: {}".format(YELLOW + players[0].name + "\033[0m", players[0].symbol))
            x = input("Enter the number of row: ")
            y = input("Enter the number of column: ")

            if (x.lower() != 'q') and (y.lower() != 'q'):
                try:
                    assert (0 <= int(x) <= 2) and (0 <= int(y) <= 2), "Entered values should be within the range (0, 2)"
            
                except AssertionError as msg:
                    print(msg)
                    continue
            
                except ValueError:
                    print(RED + "Erro: " + "\033[0m" + "Please only enter integers!!\nTry again or enter q to exit.")
                    continue
            else:
                print("Exiting game..")
                time.sleep(2)
                print("Goodbye!!")
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
                print("The position you are trying to play is already taken, try another move !!")
                continue
    
    if match.check_board() == False and (len(match.played) == 9):
        print("Draw")

    elif match.check_board() == True:
        print(f"{possible_winner.name.capitalize() } won the game")



if __name__=="__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python3 game.py <first_player_name> <second_player_name>")
        sys.exit(1)

    elif len(sys.argv) == 2:
        second_player = 'computer'
    else:
         second_player = sys.argv[2]

    first_player = sys.argv[1]
   
    tic_tac_toe(first_player.capitalize(), second_player.capitalize())

   
