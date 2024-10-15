import random


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

        self.players = random.sample([self.first_player, self.second_player], 2)
        self.players[0].symbol = 'O'
        self.players[1].symbol = 'X'

    def check_board(self):
        check = []
        for i in range(0, 7, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == 'X')
            check.append(game.dimensions[i].element == game.dimensions[i+1].element == game.dimensions[i+2].element == 'O')


        for i in range(0, 3):
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == 'X')
            check.append(game.dimensions[i].element == game.dimensions[i+3].element == game.dimensions[i+6].element == 'O')

        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == 'X')
        check.append(game.dimensions[0].element == game.dimensions[4].element == game.dimensions[8].element == 'O')

        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == 'X')
        check.append(game.dimensions[2].element == game.dimensions[4].element == game.dimensions[6].element == 'O')

        for i in check:
            if i == True:
                return True
            
        return False

    def change_element(self, row, column, element):
        for i in game.dimensions:
            if i.row == row and i.column == column:
                i.element = element

    def get_dimensions(self):
        return game.dimensions