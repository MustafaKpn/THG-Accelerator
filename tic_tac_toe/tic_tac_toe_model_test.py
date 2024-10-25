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


