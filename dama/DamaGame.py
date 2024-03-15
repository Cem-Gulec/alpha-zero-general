from __future__ import print_function
import os
import sys
from DamaLogic import Board
import numpy as np
sys.path.append('..')
from Game import Game

class Dama(Game):
    """
    This class specifies the base Game class. To define your own game, subclass
    this class and implement the functions below. This works when the game is
    two-player, adversarial and turn-based.

    Use 1 for player1 and -1 for player2.

    See othello/OthelloGame.py for an example implementation.
    """
    def __init__(self, n):
        self.n = n

    def getInitBoard(self):
        """
        Returns:
            startBoard: a representation of the board (ideally this is the form
                        that will be the input to your neural network)
        """
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        """
        Returns:
            (x,y): a tuple of board dimensions
        """
        # (a,b) tuple
        return self.n, self.n

    def getActionSize(self):
        """
        Returns:
            actionSize: number of all possible actions
        """
        # return number of actions
        return self.n**4 

    def getNextState(self, board, player, action):
        """
        Input:
            board: current board
            player: current player (1 or -1)
            action: action taken by current player

        Returns:
            nextBoard: board after applying action
            nextPlayer: player who plays in the next turn (should be -player)
        """    
        
        b = Board(self.n)
        b.pieces = np.copy(board)
        b.execute_move(action, player)
        return b.pieces, -player

    def getValidMoves(self, board, player):
        """
        Input:
            board: current board
            player: current player

        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves
        """
        # return a fixed size binary vector
        valids = [0]*self.getActionSize()
        b = Board(self.n)
        b.pieces = np.copy(board)
        legalMoves =  b.get_legal_moves(player)
        for x, y in legalMoves:
            x1, y1 = x
            x2, y2 = y
            valids[x1 + y1*self.n + x2*self.n**2 + y2*self.n**3] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.
               
        """
        b = Board(self.n)
        b.pieces = np.copy(board)

        # if b.has_legal_moves(player):
        #     return 0
        # if b.has_legal_moves(-player):
        #     return 0
        # if b.countDiff(player) > 0:
        #     return 1

        return self.temp_func(b, player)

    def temp_func(self, board, player):
        check = True
        temp = {1: 0, -1: self.n - 1}
        temp2 = {-1: -2, 1: 2}
        temp3 = {1: [-1, -2], -1: [1, 2]}

        is_game_over = temp2[player] in board.pieces[temp[player]]
        if is_game_over:
            return 1
         
        for row in board.pieces:
            for piece in row:
                if piece in temp3[player]:
                    check = False

        if check:
            return 1
        
        check = True
        temp_player = -player

        is_game_over = temp2[temp_player] in board.pieces[temp[temp_player]]
        if is_game_over:
            return -1
         
        for row in board.pieces:
            for piece in row:
                if piece in temp3[temp_player]:
                    check = False

        if check:
            return -1

        no_move_for_first_user = len(board.get_legal_moves(player)) == 0
        temp_player = -player
        no_move_for_second_user = len(board.get_legal_moves(temp_player)) == 0
    
        if no_move_for_first_user and no_move_for_second_user:
            return 1e-4

        elif no_move_for_first_user:
            return 1e-4

        return 0

    def getCanonicalForm(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)

        Returns:
            canonicalBoard: returns canonical form of board. The canonical form
                            should be independent of player. For e.g. in chess,
                            the canonical form can be chosen to be from the pov
                            of white. When the player is white, we can return
                            board as is. When the player is black, we can invert
                            the colors and return the board.
        """
        return player * board

    def getSymmetries(self, board, pi):
        """
        Input:
            board: current board
            pi: policy vector of size self.getActionSize()

        Returns:
            symmForms: a list of [(board,pi)] where each tuple is a symmetrical
                       form of the board and the corresponding pi vector. This
                       is used when training the neural network from examples.
        """
        assert(len(pi) == self.n**2+1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        """
        Input:
            board: current board

        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.
        """
        return board.tostring()
    
    def display(board):
        n = board.shape[0]

        print("   ", end="")
        for y in range(n):
            print (y,"", end="")
        print("")
        print("  ", end="")
        for _ in range(n):
            print ("-", end="-")
        print("--")
        for y in range(n):
            print(y, "|",end="")    # print the row #
            for x in range(n):
                piece = board[y][x]    # get the piece to print
                if piece == -1: print("X ",end="")
                elif piece == 1: print("X ",end="")
                else:
                    if x==n:
                        print("-",end="")
                    else:
                        print("- ",end="")
            print("|")

        print("  ", end="")
        for _ in range(n):
            print ("-", end="-")
        print("--")


x = Dama(8)
print(x.getInitBoard())
print(x.getGameEnded(x.getInitBoard(), -1))