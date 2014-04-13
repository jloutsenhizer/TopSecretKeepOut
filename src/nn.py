from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from Othello import Othello
from Player import playGame
import sys
import random
import os.path
import time

count = 0
while (True):
	#sets a ClassificationDataSet with 16 inputs and 10 outputs
	ds = ClassificationDataSet(192,64,nb_classes=64)

	#create network with no hidden layers
	nn = FeedForwardNetwork()
	#checks to see if there is already a network created
	if os.path.isfile("othelloNetwork.xml"):
		nn =  NetworkReader.readFrom("othelloNetwork.xml")

	else:
		inLayer = LinearLayer(192)
		hiddenLayer1 = SigmoidLayer(128)
		hiddenLayer2 = SoftmaxLayer(80)
		hiddenLayer3 = SigmoidLayer(33)
		outLayer = SoftmaxLayer(64)
		nn.addInputModule(inLayer)
		nn.addOutputModule(outLayer)
		nn.addModule(hiddenLayer1)
		nn.addModule(hiddenLayer2)
		nn.addModule(hiddenLayer3)
		nn.addConnection(FullConnection(inLayer, hiddenLayer1))
		nn.addConnection(FullConnection(inLayer, hiddenLayer2))
		nn.addConnection(FullConnection(hiddenLayer2, hiddenLayer3))
		nn.addConnection(FullConnection(hiddenLayer1, outLayer))
		nn.addConnection(FullConnection(hiddenLayer3, outLayer))
		nn.sortModules()

	othello = Othello()
	smartPlayer = SmartPlayer(nn,othello.boardSize)
	randomPlayer = RandomPlayer()
	randomPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]));
	smartPlayer.newGame(othello,randomPlayer.enemy);

	playGame(othello,randomPlayer,smartPlayer)
	if othello.getWinner() == randomPlayer.color:
		outcome = -1
		print "Random Player wins over Smart Player"
	elif othello.getWinner() == smartPlayer.color:
		outcome = 1
		print "Smart Player wins over Random Player"	
	else:
		outcome = 0
		print "Tie Game"

	ds = smartPlayer.gameOver(outcome)
	if (ds != None):
		trainer = BackpropTrainer(nn, dataset=ds)
		trainer.trainUntilConvergence(maxEpochs=100)
		NetworkWriter.writeToFile(nn, "othelloNetwork.xml")
		print "Terminate now to safely save"
		time.sleep(3)
		
	print count
	count += 1
