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
            if i.row == row and i.column == column:
                i.element = element
        game.played.append((row, column))

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
                    
  
