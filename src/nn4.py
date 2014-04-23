from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from SmartPlayer import SmartPlayer
from GreedyPlayer import GreedyPlayer
from TacticalPlayer import TacticalPlayer
from Othello import Othello
from Player import playGame
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
    if os.path.isfile("othelloNetwork4.xml"):
		if flag1 == 0:
			flag1 = 1		
			print "Getting network from file..."

		nn =  NetworkReader.readFrom("othelloNetwork4.xml")
		
    else:
        print "No network present, building new one..."
        inLayer = LinearLayer(192)
        hiddenLayer1 = SigmoidLayer(50)
        hiddenLayer2 = SigmoidLayer(250)
        hiddenLayer3 = SigmoidLayer(150)
        hiddenLayer4 = SigmoidLayer(200)
        hiddenLayer5 = SigmoidLayer(100)
        outLayer = SoftmaxLayer(64)
        nn.addInputModule(inLayer)
        nn.addOutputModule(outLayer)
        nn.addModule(hiddenLayer1)
        nn.addModule(hiddenLayer2)
        nn.addModule(hiddenLayer3)
        nn.addModule(hiddenLayer4)
        nn.addModule(hiddenLayer5)
        nn.addConnection(FullConnection(inLayer, hiddenLayer1))
        nn.addConnection(FullConnection(inLayer, hiddenLayer2))
        nn.addConnection(FullConnection(hiddenLayer1, hiddenLayer3))
        nn.addConnection(FullConnection(hiddenLayer2, hiddenLayer3))
        nn.addConnection(FullConnection(hiddenLayer2, hiddenLayer5))
        nn.addConnection(FullConnection(hiddenLayer3, hiddenLayer4))
        nn.addConnection(FullConnection(hiddenLayer3, hiddenLayer5))
        nn.addConnection(FullConnection(hiddenLayer3, outLayer))
        nn.addConnection(FullConnection(hiddenLayer4, outLayer))				
        nn.addConnection(FullConnection(hiddenLayer5, outLayer))
        nn.sortModules()

    othello = Othello()
    smartPlayer = SmartPlayer(nn,othello.boardSize)
    tacticalPlayer = TacticalPlayer()
    tacticalPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]));
    smartPlayer.newGame(othello,tacticalPlayer.enemy);

    playGame(othello,tacticalPlayer,smartPlayer)
    if othello.getWinner() == tacticalPlayer.color:
        outcome = -1
        print "Tactical Player wins over Network Player 4"
        count += 1
        semicount += 1
	
    elif othello.getWinner() == smartPlayer.color:
        outcome = 1
        print "Network Player 4 wins over Tactical Player"		
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
        trainer.trainUntilConvergence(maxEpochs=50)
        NetworkWriter.writeToFile(nn, "othelloNetwork4.xml")
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

