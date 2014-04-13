from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet
from Othello import Othello
import random

class RandomPlayer: 	
    def newGame(self, game, color):
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            self.enemy = self.game.BLACK_PLAYER
        else:
            self.enemy = self.game.WHITE_PLAYER

    def getMove(self):  #returns the network's choice for "best" move
		return random.choice(self.game.getAllPossibleMoves(self.color));
        

