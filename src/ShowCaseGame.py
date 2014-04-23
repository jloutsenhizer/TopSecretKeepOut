from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from GreedyPlayer import GreedyPlayer
from Othello import Othello
from Player import playGame
from HumanPlayer import HumanPlayer
from pybrain.tools.customxml.networkreader import NetworkReader
from TacticalPlayer import TacticalPlayer
import random
import time

nn =  NetworkReader.readFrom("othelloNetwork.xml")
player1 = SmartPlayer(nn,8)  #change this to change the opponent to be testing against
player2 = RandomPlayer()

othello = Othello()

othello.resetGame()
player1.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
player2.newGame(othello,player1.enemy)

while not othello.isGameOver():
    if (player1.color == othello.WHITE_PLAYER):
        print "Neural Network is white"
    else:
        print "Neural Network is black"
    othello.printBoard()
    time.sleep(1)
    if (othello.whoGoesNext() == player1.color):
        move = player1.getMove()
        othello.makeMove(move[0],move[1],player1.color)
    else:
        move = player2.getMove()
        othello.makeMove(move[0],move[1],player2.color)

if othello.getWinner() == player1.color:
    print "Neural network won!"
elif othello.getWinner() == player2.color:
    print "Neural network lost!"
else:
    print "Tie game! :("
othello.printBoard()