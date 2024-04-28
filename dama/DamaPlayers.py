import numpy as np
#from .Digits import int2base

# minimax alpha-beta pruningle belirli bir derinliğe kadar bakan bir player yaratılabilir

class GreedyDamaPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        candidates = []
        for a in range(self.game.getActionSize()):
            if valids[a]==0:
                continue
            nextBoard, _ = self.game.getNextState(board, 1, a)
            score = self.game.getGameEnded(nextBoard, 1)
            candidates += [(-score, a)]
        candidates.sort()
        return candidates[0][1]

class RandomDamaPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a

class HumanDamaPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        # display(board)
        pass