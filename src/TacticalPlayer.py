from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet
from Othello import Othello
import random

class TacticalPlayer: 	
    def newGame(self, game, color):
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            self.enemy = self.game.BLACK_PLAYER
        else:
            self.enemy = self.game.WHITE_PLAYER
            


    def isCorner(self, x, y, end): # are the coordinates for a corner
        if (x == 0 and y == 0):
            return True
        if (x == 0 and y == end):
            return True
        if (x == end and y == 0):
            return True
        if (x == end and y == end):
            return True
        
        return False
        

        
    def notDanger(self, x, y, end): # is it next to a corner
    
        e = end - 1
        
        if x == 0:
            if y == 1 or y == e:
                return False
        if x == 1:
            if y == 0 or y == 1 or y == e or y == end:
                return False
        if x == e:
            if y == 0 or y == 1 or y == e or y == end:
                return False
        if x == end:
            if y == 1 or y == e:
                return False
                
        return True



    def isSide(self, x, y, end):
    
        if x == 0 or x == end:
            if self.notDanger(x, y, end):
                return True
                
        if y == 0 or y == end:
            if self.notDanger(x, y, end):
                return True
                
        return False



    def getMove(self):  #returns the network's choice for "best" move
        max = 0
        move = (-1,-1)
        end = self.game.boardSize
        options = self.game.getAllPossibleMoves(self.color)
        
        # first look for corners
        for i in range(len(options)):
            x, y = options[i]
            
            if self.isCorner(x, y, end):
            
                val = len(self.game.getPointsOfChange(x, y, self.color))
            
                if val > max:
                    max = val
                    move = (x, y)
                
        if max != 0:
            x, y = move
            #print "(", x, ",", y, ")"
            return move
                
        # next look for side spaces not adjacent to corners
        for j in range(len(options)):
            x, y = options[j]
            
            if self.isSide(x, y, end):

                val = len(self.game.getPointsOfChange(x, y, self.color))
            
                if val > max:
                    max = val
                    move = (x, y)
                
        if max != 0:
            x, y = move
            #print "(", x, ",", y, ")"
            return move
                
        # next go greedy while avoiding corner adjacent places
        for k in range(len(options)):
            x, y = options[k]
            
            if self.notDanger(x, y, end):
            
                val = len(self.game.getPointsOfChange(x, y, self.color))
            
                if val > max:
                    max = val
                    move = (x, y)
                
        if max != 0:
            x, y = move
            #print "(", x, ",", y, ")"
            return move
            
        # just take whatever we can get
        for l in range(len(options)):
            x, y = options[l]
            val = len(self.game.getPointsOfChange(x, y, self.color))
            
            if val > max:
                max = val
                move = (x, y)
                
        x, y = move
        #print "(", x, ",", y, ")"
        return move




























