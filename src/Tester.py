from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from Othello import Othello
from Player import playGame
from pybrain.tools.customxml.networkreader import NetworkReader
import random

randomPlayer1 = RandomPlayer()
randomPlayer2 = RandomPlayer()

nn =  NetworkReader.readFrom("othelloNetwork.xml")
smartPlayer = SmartPlayer(nn,8)
othello = Othello()

rvrP1Wins = 0
rvrP2Wins = 0
rvrTies = 0
nvrP1Wins = 0
nvrP2Wins = 0
nvrTies = 0

for x in xrange(0,100):#run 100 gamess
	print "Iteration " + str(x+1)
	#print "Random vs Random"
	othello.resetGame()
	randomPlayer1.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
	randomPlayer2.newGame(othello,randomPlayer1.enemy)
	playGame(othello,randomPlayer1,randomPlayer2)
	if othello.getWinner() == randomPlayer1.color:
		rvrP1Wins += 1
		#print "Random Player 1 is vicotorious! Glory to the RNG!"
	elif othello.getWinner() == randomPlayer2.color:
		rvrP2Wins += 1
		#print "Random Player 2 is victorious! Glory to the RNG!"
	else:
		rvrTies += 1
		#print "Tie game! :("
	othello.resetGame()
	smartPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
	randomPlayer2.newGame(othello,smartPlayer.enemy)
	playGame(othello,smartPlayer,randomPlayer2)
	if othello.getWinner() == smartPlayer.color:
		nvrP1Wins += 1
		#print "Smart Player is victorious! Glory to the Machine Brains!"
	elif othello.getWinner() == randomPlayer2.color:
		nvrP2Wins += 1
		#print "Random Player is victorious!"
	else:
		nvrTies += 1
		#print "Tie game! D:"

print "Random vs Random win rate: " + str(rvrP1Wins / float(rvrP1Wins + rvrP2Wins + rvrTies))
print "Network vs Random win rate: " + str(nvrP1Wins / float(nvrP1Wins + nvrP2Wins + nvrTies))


		
	

