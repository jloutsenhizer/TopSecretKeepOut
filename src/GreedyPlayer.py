from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet
from Othello import Othello
import random

class GreedyPlayer: 	
    def newGame(self, game, color):
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            self.enemy = self.game.BLACK_PLAYER
        else:
            self.enemy = self.game.WHITE_PLAYER

    def getMove(self):  #returns the network's choice for "best" move
        max = 0
        move = (-1,-1)
        options = self.game.getAllPossibleMoves(self.color)
        
        for i in range(len(options)):
            x, y = options[i]
            val = len(self.game.getPointsOfChange(x, y, self.color))
            
            if val > max:
                max = val
                move = (x, y)
                
        return move