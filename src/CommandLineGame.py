from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from GreedyPlayer import GreedyPlayer
from Othello import Othello
from Player import playGame
from HumanPlayer import HumanPlayer
from pybrain.tools.customxml.networkreader import NetworkReader
from TacticalPlayer import TacticalPlayer
import random

#nn =  NetworkReader.readFrom("othelloNetwork.xml")
#opponentPlayer = SmartPlayer(nn,8)  #change this to change the opponent to be testing against
opponentPlayer = TacticalPlayer()
humanPlayer = HumanPlayer()

othello = Othello()

othello.resetGame()
humanPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
opponentPlayer.newGame(othello,humanPlayer.enemy)
playGame(othello,humanPlayer,opponentPlayer)

if othello.getWinner() == humanPlayer.color:
    print "You won!"
elif othello.getWinner() == opponentPlayer.color:
    print "You lost!"
else:
    print "Tie game! :("