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
        outLayer = SoftmaxLayer(64)

        nn.addInputModule(inLayer)
        nn.addOutputModule(outLayer)
		
        for i in range(6):
		    for j in range(6):
		    	#creates 3x3 chunks
		    	from1 = (j * i) + j
		    	to1 = from1 + 9
		    	
		    	from2 = (j * (i+1)) + j
		    	to2 = from2 + 9
		    	
		    	from3 = (j * (i+2)) + j
		    	to3 = from2 + 9
		    	
		    	#connects chunks to a hidden layer		    	
		    	lay = SigmoidLayer(100)
		    	
		    	nn.addModule(lay)
		    	
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from1, inSliceTo=to1))
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from2, inSliceTo=to2))
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from3, inSliceTo=to3))
				
				nn.addConnection(FullConnection(lay, outLayer))
								
				
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

