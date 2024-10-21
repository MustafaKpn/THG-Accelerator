from tic_tac_toe_model import *
import random
import sys

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
