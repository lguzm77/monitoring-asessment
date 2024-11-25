
class TicTacToe:

    def __init__(self, board):
        self.board = board 
        self.CORNERS = [(0,0) , (0, 3) , (3,0) , (3,3) ]
        self.DIAGONALS = [(0,3), (1,2), (2,2), (3,0) ]

    def checkRow(self,row, playerToCheck):
        for c in range(1,len(self.board[0])):
            if self.board[row][c] != playerToCheck:
                return False 
        return True


    def checkColumn(self,column, playerToCheck):
        for r in range(1, len(self.board)):
            if self.board[r][column] != playerToCheck:
                return False 
        return True

    def checkTwoByTwoBox(self,row,column):
        player = self.board[row][column]

        # Assume current grid is top left 
        if 0<= row < len(self.board) - 1 and 0 <= column < len(self.board[0]) - 1:
            return self.board[row + 1][column] == player and self.board[row][column+1] == player and self.board[row+1][column+1] == player

        return False

    def checkCorners(self, playerToCheck):
        player = self.board[0][0]
        for i in range(1, len(self.CORNERS)):
            r,c = self.CORNERS[i]
            if self.board[r][c] != playerToCheck: 
                return False 
        return True
    
    def checkLeftDiagonal(self, playerToCheck):
        player = self.board[0][0]
        for i in range(len(self.board)):
            if self.board[i][i] != playerToCheck:
                return False
        return True
    def checkRightDiagonal(self, playerToCheck):
        player = self.board[0][3]
        
        for i in range(1,len(self.DIAGONALS)):
            r,c = self.DIAGONALS[i]
            for i in range(len(self.board)):
                if self.board[r][c] != playerToCheck:
                    return False 
        return True

    def checkWinner(self) :
        # Returns the player than wins, None if there is no winner
        # Check each winning condition
        # horizontal, vertical, diagonal , 2x2 box, CORNERS 
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                player = self.board[r][c]
                if player == 0:
                    continue
                if c == 0:
                    # iterate each row
                    if self.checkRow(r, player):
                        return player
                if r == 0:
                    #iterate each column
                    if self.checkColumn(c, player):
                        return player 
                if (r,c) in self.CORNERS:
                    if self.checkCorners(player):
                        return player
                if (r,c) in self.DIAGONALS:
                    if self.checkRightDiagonal(player) or self.checkLeftDiagonal(player):
                        return player
                if self.checkTwoByTwoBox(r,c):
                    return player
        return None
    

    def anyMovesLeft(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == 0:
                    return True
        return False 
          
    def isGameOver(self):
        # If there are no moves left, it is over
        return not self.anyMovesLeft() 
# Tests 
import unittest

class TestTicTacToe(unittest.TestCase):
    def test_check_tie(self):
        board = [
            [2,2,1,1],
            [1,1,1,2],
            [2,1,2,2],
            [1,1,1,2]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), None)


    def test_check_horizontal(self):
        board = [
            [0,0,0,0],
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)
    
    def test_vertical(self):
        board = [
            [0,0,1,0],
            [1,2,1,1],
            [0,0,1,0],
            [0,0,1,0]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)

    def test_corners(self):
        board = [
            [1,0,2,1],
            [1,2,1,1],
            [0,0,1,0],
            [1,0,1,1]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)
    def test_left_diagonal(self):

        board = [
                [1,0,2,2],
                [1,1,2,1],
                [0,0,1,0],
                [1,0,1,1]
                ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)
        
    def test_right_diagonal(self):
        board = [
                [1,0,2,1],
                [1,2,1,1],
                [0,1,1,0],
                [1,0,2,2]
                ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)

    def test_two_by_two_box(self):
        board = [
                [1,1,2,1],
                [2,2,1,1],
                [1,1,2,0],
                [1,1,2,2]
                ]
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), 1)

class TestAnyMovesLeft(unittest.TestCase):

    def test_any_moves_left(self):
        board = [
            [1,2,2,1],
            [2,0,1,2],
            [2,1,1,2],
            [2,1,1,2]
         ]
        game = TicTacToe(board)
        anyMovesLeft = game.anyMovesLeft()
        self.assertEqual(anyMovesLeft,True)

    def test_any_moves_left_full_board(self):
        # Generates a 4x4 board all populated by 1
        board = [[1 for i in range(4)] for i in range(4) ]
        game = TicTacToe(board)
        anyMovesLeft = game.anyMovesLeft()
        self.assertEqual(anyMovesLeft, False)

class TestIsGameOver(unittest.TestCase):
    def test_is_game_over_empty_board(self):
        board = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
         ]
        game = TicTacToe(board)
        self.assertEqual(game.isGameOver(),False)
    def test_is_game_over(self):
        board = [
             [1,2,1,1],
            [1,2,1,1],
            [1,2,2,2],
            [1,1,2,1]
        ]
        game = TicTacToe(board)
        self.assertEqual(game.isGameOver(), True)
        
if __name__ == "__main__":
    unittest.main()