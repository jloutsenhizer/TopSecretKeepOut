from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from SmartPlayer import SmartPlayer
from GreedyPlayer import GreedyPlayer
from Othello import Othello
from Player import playGame
from TacticalPlayer import TacticalPlayer
import sys
import random
import os.path
import time

wincnt = 0
count = 0
flag1 = 0
semicount = 0
semiwincnt = 0
while (True):
    #sets a ClassificationDataSet with 16 inputs and 10 outputs
    ds = ClassificationDataSet(192,64,nb_classes=64)

    #create network with no hidden layers
    nn = FeedForwardNetwork()
    #checks to see if there is already a network created
    if os.path.isfile("othelloNetwork5.xml"):
		if flag1 == 0:
			flag1 = 1		
			print "Getting network from file..."

		nn =  NetworkReader.readFrom("othelloNetwork5.xml")
		
    else:
        print "No network present, building new one..."
        inLayer = LinearLayer(192)
        hiddenLayer1 = SigmoidLayer(50)
        hiddenLayer2 = SigmoidLayer(50)
        hiddenLayer3 = SigmoidLayer(50)
        hiddenLayer4 = SigmoidLayer(50)

        outLayer = SoftmaxLayer(64)
        nn.addInputModule(inLayer)
        nn.addOutputModule(outLayer)
        nn.addModule(hiddenLayer1)
		
        nn.addConnection(FullConnection(inLayer, hiddenLayer1, inSliceTo=16))
        nn.addConnection(FullConnection(inLayer, hiddenLayer1, inSliceFrom=16, inSliceTo=32))
        nn.addConnection(FullConnection(inLayer, hiddenLayer1, inSliceFrom=32, insliceTo=48))
        nn.addConnection(FullConnection(inLayer, hiddenLayer1, inSliceFrom=48))
        nn.addConnection(FullConnection(hiddenLayer1, outLayer))
        nn.sortModules()

    othello = Othello()
    smartPlayer = SmartPlayer(nn,othello.boardSize)
    greedyPlayer = TacticalPlayer()
    greedyPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]));
    smartPlayer.newGame(othello,greedyPlayer.enemy);

    playGame(othello,greedyPlayer,smartPlayer)
    if othello.getWinner() == greedyPlayer.color:
        outcome = -1
        print "Tactical Player wins over Network Player 5"
        count += 1
        semicount += 1
	
    elif othello.getWinner() == smartPlayer.color:
        outcome = 1
        print "Network Player 5 wins over Tactical Player"		
    	count += 1
        wincnt += 1
        semicount += 1
        semiwincnt += 1

    else:
        outcome = 0
        print "Tie Game"


    ds = smartPlayer.gameOver(outcome)
    if (ds != None):
        trainer = BackpropTrainer(nn, dataset=ds)
        trainer.trainUntilConvergence(maxEpochs=200)
        NetworkWriter.writeToFile(nn, "othelloNetwork5.xml")
    #print "Terminate now to safely save"
    #time.sleep(3)
	
	perc = float(wincnt) / float(count)
	perc *= float(100)
    print perc

    if semicount == 20:
		semiperc = float(semiwincnt) / float(semicount)
		semiperc *= float(100)
		print "Last ", semicount, " games: ", semiperc, "%"
		semicount = 0
		semiwincnt = 0

