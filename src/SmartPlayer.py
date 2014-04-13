from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import ClassificationDataSet
from Othello import Othello

'''
	The "Smart"Player class uses the current network to pick moves and remembers those moves.
	At the end of the game, the remembered moves' weights are updated based on the outcome


	Note:  I'd like to draw your attention to the gameOver method.  I made some design choices here about the update rules; we should discuss any disagreements.
'''
class SmartPlayer:
    def __init__(self, network, boardSize):
        self.boardSize = boardSize
        self.network = network
        self.data = []

    def newGame(self, game, color):
        self.data = []
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            self.enemy = self.game.BLACK_PLAYER
        else:
            self.enemy = self.game.WHITE_PLAYER

    def gameOver(self, outcome): #returns a dataset updated based on the argument outcome (-1 loss, 0 draw, 1 win)
        if outcome == 0:
            return None #opted to return none since the new dataset would be the same
        self.ds = ClassificationDataSet(self.boardSize * self.boardSize * 3, self.boardSize * self.boardSize,nb_classes=64) #might consider having boardSize * boardSize * 3 has input
        for t in self.data: #go through all the board configurations we collected from this game and update our desired outcomes
            newTarget = []
            for y in xrange(0,self.boardSize):
                for x in xrange(0,self.boardSize):
                    if (t[1][0] == x and t[1][1] == y):
                        if (outcome == 1):
                            newTarget.append((t[2][y*8+x] + 1) / 2)  #increase the preference of this move
                        else:
                            newTarget.append((t[2][y*8+x] + 0) / 2) #decrease preference of this move
                    else:
                        newTarget.append(t[2][y*8+x]) #right now we don't do anything to the other options. we could decrease preference of these moves
            self.ds.addSample(t[0], newTarget)
        return self.ds;

    def getMove(self):  #returns the network's choice for "best" move
        data = [];
        for y in xrange(0,self.boardSize):
            for x in xrange(0,self.boardSize):          #Right now we're building 8x8 data inputs, we might want to use 8x8x3 since there's no natural ordering
                piece = self.game.getPieceAtLocation(x,y);
                if (piece == self.color):
                    data.append(1)
                else:
                    data.append(0)
                if(piece == self.enemy):
                    data.append(1)
                else:
                    data.append(0)
                if (piece == self.game.NO_PIECE):
                    data.append(1)
                else:
                    data.append(0)
        preds = self.network.activate(data);

        maxVal = -1
        bestMove = None

        for move in self.game.getAllPossibleMoves(self.color):           #iterate through all the possible moves and pick the one with the highest output value
            if (preds[move[1] * self.boardSize + move[0]] > maxVal):
                bestMove = move
                maxVal = preds[move[1] * self.boardSize + move[0]]

        self.data.append((data, bestMove, preds))
        return bestMove

