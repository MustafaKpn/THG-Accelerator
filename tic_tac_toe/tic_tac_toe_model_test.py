from tic_tac_toe_model import player, position, game

class TestTicTacToe:
    
    def setup_method(self):
        """Set up the initial game state for each test."""
        self.player1 = player("Phil", "X")
        self.player2 = player("James", "O")
        self.match = game(self.player1, self.player2)

    def test_player_creation(self):
        assert self.player1.name == "Phil"
        assert self.player1.symbol == "X"
        assert self.player2.name == "James"
        assert self.player2.symbol == "O"

    def test_position_creation(self):
        pos = position(0, 0, "X")
        assert pos.row == 0
        assert pos.column == 0
        assert pos.element == "X"

    def test_make_board(self):
        assert len(game.dimensions) == 9
        assert game.dimensions[0].row == 0
        assert game.dimensions[0].column == 0
        assert game.dimensions[8].row == 2
        assert game.dimensions[8].column == 2

    def test_change_element(self):
        self.match.change_element(0, 0, "X")
        assert game.dimensions[0].element == "X"
        assert (0, 0) in game.played

    def test_allow_move(self):
        self.match.change_element(0, 0, "X")
        assert not self.match.allow_move(0, 0)  
        assert self.match.allow_move(1, 1)      

    def test_check_board(self):
        self.match.change_element(0, 0, "X")
        self.match.change_element(0, 1, "X")
        self.match.change_element(0, 2, "X")
        assert self.match.check_board()  


import pytest

@pytest.fixture
def setup_game():
    # Set up a game with two players
    player1 = player("Alice", "X")
    player2 = player("Bob", "O")
    test_game = game(player1, player2)
    
    # Return the initialized game object
    return test_game

def test_solve_for_weights_empty_board(setup_game):
    test_game = setup_game
    
    # Ensure the board is initially empty
    for pos in test_game.dimensions:
        pos.element = '?'
    
    test_game.solve_for_weights()

    # Check if the first move is made correctly
    assert any(pos.element == test_game.player2.symbol for pos in test_game.dimensions), "The move wasn't made correctly for an empty board."

def test_solve_for_weights_block_enemy_win(setup_game):
    test_game = setup_game
    
    # Simulate the enemy ('X') having two in a row, needing a block
    test_game.dimensions[0].element = 'X'
    test_game.dimensions[1].element = 'X'
    test_game.dimensions[2].element = '?'
    
    test_game.solve_for_weights()

    # Check if the move was placed to block the win
    assert test_game.dimensions[2].element == test_game.player2.symbol, "The AI didn't block the enemy's win."

def test_solve_for_weights_advance_own_win(setup_game):
    test_game = setup_game
    
    # Simulate the AI ('O') having two in a row, needing to win
    test_game.dimensions[0].element = 'O'
    test_game.dimensions[1].element = 'O'
    test_game.dimensions[2].element = '?'
    
    test_game.solve_for_weights()

    # Check if the move was placed to win
    assert test_game.dimensions[2].element == test_game.player2.symbol, "The AI didn't complete its winning move."
