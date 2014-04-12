from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet
from Othello import Othello
import random

class RandomPlayer:
    def __init__(self):

    def newGame(self, game, color):
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            self.enemy = self.game.BLACK_PLAYER
        else:
            self.enemy = self.game.WHITE_PLAYER

    def gameOver(self, outcome): #returns a dataset updated based on the argument outcome (-1 loss, 0 draw, 1 win)
       

	def getMoves(self): #returns a list of (x, y) pairs that are the viable moves for the argument board configuration
		return self.game.getAllPossibleMoves(self.color)

    def getMove(self):  #returns the network's choice for "best" move
	return random.choice(self.getMoves());
        

