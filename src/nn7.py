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
    if os.path.isfile("othelloNetwork7.xml"):
		if flag1 == 0:
			flag1 = 1		
			print "Getting network from file..."

		nn =  NetworkReader.readFrom("othelloNetwork7.xml")
		
    else:
        print "No network present, building new one..."
        inLayer = LinearLayer(192)
        outLayer = SoftmaxLayer(64)
        hidLay1 = SigmoidLayer(50)
        hidLay2 = SigmoidLayer(50)
        hidLay3 = SigmoidLayer(50)
        hidLay4 = SigmoidLayer(50)
        hidLay5 = SigmoidLayer(50)
        hidLay6 = SigmoidLayer(50)
        hidLay7 = SigmoidLayer(50)
        hidLay8 = SigmoidLayer(50)
        hidLay9 = SigmoidLayer(50)
        hidLay10 = SigmoidLayer(50)
        hidLay11 = SigmoidLayer(50)
        hidLay12 = SigmoidLayer(50)
        hidLay13 = SigmoidLayer(50)
        hidLay14 = SigmoidLayer(50)
        hidLay15 = SigmoidLayer(50)
        hidLay16 = SigmoidLayer(50)
        hidLay17 = SigmoidLayer(50)
        hidLay18 = SigmoidLayer(50)
        hidLay19 = SigmoidLayer(50)
        hidLay20 = SigmoidLayer(50)
        hidLay21 = SigmoidLayer(50)
        hidLay22 = SigmoidLayer(50)
        hidLay23 = SigmoidLayer(50)
        hidLay24 = SigmoidLayer(50)
        hidLay25 = SigmoidLayer(50)
        
        h2hidLay1 = SigmoidLayer(75)
        h2hidLay2 = SigmoidLayer(75)
        h2hidLay3 = SigmoidLayer(75)
        h2hidLay4 = SigmoidLayer(75)
        h2hidLay5 = SigmoidLayer(75)
        h2hidLay6 = SigmoidLayer(75)
        h2hidLay7 = SigmoidLayer(75)
        h2hidLay8 = SigmoidLayer(75)
        h2hidLay9 = SigmoidLayer(75)
        h2hidLay10 = SigmoidLayer(75)
        h2hidLay11 = SigmoidLayer(75)
        h2hidLay12 = SigmoidLayer(75)
        h2hidLay13 = SigmoidLayer(75)
        h2hidLay14 = SigmoidLayer(75)
        h2hidLay15 = SigmoidLayer(75)
        h2hidLay16 = SigmoidLayer(75)
        
        h3hidLay1 = SigmoidLayer(100)
        h3hidLay2 = SigmoidLayer(100)
        h3hidLay3 = SigmoidLayer(100)
        h3hidLay4 = SigmoidLayer(100)
        h3hidLay5 = SigmoidLayer(100)
        h3hidLay6 = SigmoidLayer(100)
        h3hidLay7 = SigmoidLayer(100)
        h3hidLay8 = SigmoidLayer(100)
        h3hidLay9 = SigmoidLayer(100)
        
        h4hidLay1 = SigmoidLayer(150)
        h4hidLay2 = SigmoidLayer(150)
        h4hidLay3 = SigmoidLayer(150)
        h4hidLay4 = SigmoidLayer(150)
        
        nn.addModule(hidLay1)
        nn.addModule(hidLay2)
        nn.addModule(hidLay3)
        nn.addModule(hidLay4)
        nn.addModule(hidLay5)
        nn.addModule(hidLay6)
        nn.addModule(hidLay7)
        nn.addModule(hidLay8)
        nn.addModule(hidLay9)
        nn.addModule(hidLay10)
        nn.addModule(hidLay11)
        nn.addModule(hidLay12)
        nn.addModule(hidLay13)
        nn.addModule(hidLay14)
        nn.addModule(hidLay15)
        nn.addModule(hidLay16)
        nn.addModule(hidLay17)
        nn.addModule(hidLay18)
        nn.addModule(hidLay19)
        nn.addModule(hidLay20)
        nn.addModule(hidLay21)
        nn.addModule(hidLay22)
        nn.addModule(hidLay23)
        nn.addModule(hidLay24)
        nn.addModule(hidLay25)
        
        nn.addModule(h2hidLay1)
        nn.addModule(h2hidLay2)
        nn.addModule(h2hidLay3)
        nn.addModule(h2hidLay4)
        nn.addModule(h2hidLay5)
        nn.addModule(h2hidLay6)
        nn.addModule(h2hidLay7)
        nn.addModule(h2hidLay8)
        nn.addModule(h2hidLay9)
        nn.addModule(h2hidLay10)
        nn.addModule(h2hidLay11)
        nn.addModule(h2hidLay12)
        nn.addModule(h2hidLay13)
        nn.addModule(h2hidLay14)
        nn.addModule(h2hidLay15)
        nn.addModule(h2hidLay16)
        
        nn.addModule(h3hidLay1)
        nn.addModule(h3hidLay2)
        nn.addModule(h3hidLay3)
        nn.addModule(h3hidLay4)
        nn.addModule(h3hidLay5)
        nn.addModule(h3hidLay6)
        nn.addModule(h3hidLay7)
        nn.addModule(h3hidLay8)
        nn.addModule(h3hidLay9)
        
        nn.addModule(h4hidLay1)
        nn.addModule(h4hidLay2)
        nn.addModule(h4hidLay3)
        nn.addModule(h4hidLay4)
        
        nn.addInputModule(inLayer)
        nn.addOutputModule(outLayer)
        
        cnt = 0
		
        for i in range(6):
		    for j in range(6):
		    	#creates 36 3x3 boards
		    	from1 = (j * i) + j
		    	to1 = from1 + 9
		    	
		    	from2 = (j * (i+1)) + j
		    	to2 = from2 + 9
		    	
		    	from3 = (j * (i+2)) + j
		    	to3 = from2 + 9
		    	
		    	#connects chunks to a hidden layer		    	
		    	lay = SigmoidLayer(30)
		    	
		    	nn.addModule(lay)
		    	
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from1, inSliceTo=to1))
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from2, inSliceTo=to2))
		    	nn.addConnection(FullConnection(inLayer, lay, inSliceFrom=from3, inSliceTo=to3))
		    	
		    	cnt += 1
		    	#manually adds in to 1st hidden layer (25 4x4 boards)
		    	if (cnt == 1 or cnt == 2 or cnt == 7 or cnt == 8):
		    		nn.addConnection(FullConnection(lay, hidLay1))
				if (cnt == 2 or cnt == 3 or cnt == 8 or cnt == 9):
					nn.addConnection(FullConnection(lay, hidLay2))
				if (cnt == 3 or cnt == 4 or cnt == 9 or cnt == 10):
					nn.addConnection(FullConnection(lay, hidLay3))
				if (cnt == 4 or cnt == 5 or cnt == 10 or cnt == 11):
					nn.addConnection(FullConnection(lay, hidLay4))
				if (cnt == 5 or cnt == 6 or cnt == 11 or cnt == 12):
					nn.addConnection(FullConnection(lay, hidLay5))	
						
				if (cnt == 7 or cnt == 8 or cnt == 13 or cnt == 14):
					nn.addConnection(FullConnection(lay, hidLay6))		
				if (cnt == 8 or cnt == 9 or cnt == 14 or cnt == 15):
					nn.addConnection(FullConnection(lay, hidLay7))		
				if (cnt == 9 or cnt == 10 or cnt == 15 or cnt == 16):
					nn.addConnection(FullConnection(lay, hidLay8))		
				if (cnt == 10 or cnt == 1 or cnt == 16 or cnt == 17):
					nn.addConnection(FullConnection(lay, hidLay9))		
				if (cnt == 11 or cnt == 12 or cnt == 17 or cnt == 18):
					nn.addConnection(FullConnection(lay, hidLay10))	
						
				if (cnt == 13 or cnt == 14 or cnt == 19 or cnt == 20):
					nn.addConnection(FullConnection(lay, hidLay11))		
				if (cnt == 14 or cnt == 15 or cnt == 20 or cnt == 21):
					nn.addConnection(FullConnection(lay, hidLay12))		
				if (cnt == 15 or cnt == 16 or cnt == 21 or cnt == 22):
					nn.addConnection(FullConnection(lay, hidLay13))		
				if (cnt == 16 or cnt == 17 or cnt == 22 or cnt == 23):
					nn.addConnection(FullConnection(lay, hidLay14))		
				if (cnt == 17 or cnt == 18 or cnt == 23 or cnt == 24):
					nn.addConnection(FullConnection(lay, hidLay15))	
						
				if (cnt == 19 or cnt == 20 or cnt == 25 or cnt == 26):
					nn.addConnection(FullConnection(lay, hidLay16))		
				if (cnt == 20 or cnt == 21 or cnt == 26 or cnt == 27):
					nn.addConnection(FullConnection(lay, hidLay17))		
				if (cnt == 21 or cnt == 22 or cnt == 27 or cnt == 28):
					nn.addConnection(FullConnection(lay, hidLay18))		
				if (cnt == 22 or cnt == 23 or cnt == 28 or cnt == 29):
					nn.addConnection(FullConnection(lay, hidLay19))		
				if (cnt == 23 or cnt == 24 or cnt == 29 or cnt == 30):
					nn.addConnection(FullConnection(lay, hidLay20))	
						
				if (cnt == 25 or cnt == 26 or cnt == 31 or cnt == 32):
					nn.addConnection(FullConnection(lay, hidLay21))		
				if (cnt == 26 or cnt == 27 or cnt == 32 or cnt == 33):
					nn.addConnection(FullConnection(lay, hidLay22))		
				if (cnt == 27 or cnt == 28 or cnt == 33 or cnt == 34):
					nn.addConnection(FullConnection(lay, hidLay23))		
				if (cnt == 28 or cnt == 29 or cnt == 34 or cnt == 35):
					nn.addConnection(FullConnection(lay, hidLay24))		
				if (cnt == 29 or cnt == 30 or cnt == 35 or cnt == 36):
					nn.addConnection(FullConnection(lay, hidLay25))

	#manually creates connections for 2nd hidden layer (16 5x5 boards)
	nn.addConnection(FullConnection(hidLay1, h2hidLay1))
	nn.addConnection(FullConnection(hidLay2, h2hidLay1))
	nn.addConnection(FullConnection(hidLay6, h2hidLay1))
	nn.addConnection(FullConnection(hidLay7, h2hidLay1))
	
	nn.addConnection(FullConnection(hidLay2, h2hidLay2))
	nn.addConnection(FullConnection(hidLay3, h2hidLay2))
	nn.addConnection(FullConnection(hidLay7, h2hidLay2))
	nn.addConnection(FullConnection(hidLay8, h2hidLay2))
	
	nn.addConnection(FullConnection(hidLay3, h2hidLay3))
	nn.addConnection(FullConnection(hidLay4, h2hidLay3))
	nn.addConnection(FullConnection(hidLay8, h2hidLay3))
	nn.addConnection(FullConnection(hidLay9, h2hidLay3))
	
	nn.addConnection(FullConnection(hidLay4, h2hidLay4))
	nn.addConnection(FullConnection(hidLay5, h2hidLay4))
	nn.addConnection(FullConnection(hidLay9, h2hidLay4))
	nn.addConnection(FullConnection(hidLay10, h2hidLay4))
	
	nn.addConnection(FullConnection(hidLay6, h2hidLay5))
	nn.addConnection(FullConnection(hidLay7, h2hidLay5))
	nn.addConnection(FullConnection(hidLay11, h2hidLay5))
	nn.addConnection(FullConnection(hidLay12, h2hidLay5))
	
	nn.addConnection(FullConnection(hidLay7, h2hidLay6))
	nn.addConnection(FullConnection(hidLay8, h2hidLay6))
	nn.addConnection(FullConnection(hidLay12, h2hidLay6))
	nn.addConnection(FullConnection(hidLay13, h2hidLay6))
	
	nn.addConnection(FullConnection(hidLay8, h2hidLay7))
	nn.addConnection(FullConnection(hidLay9, h2hidLay7))
	nn.addConnection(FullConnection(hidLay13, h2hidLay7))
	nn.addConnection(FullConnection(hidLay14, h2hidLay7))
	
	nn.addConnection(FullConnection(hidLay9, h2hidLay8))
	nn.addConnection(FullConnection(hidLay10, h2hidLay8))
	nn.addConnection(FullConnection(hidLay14, h2hidLay8))
	nn.addConnection(FullConnection(hidLay15, h2hidLay8))
	
	nn.addConnection(FullConnection(hidLay11, h2hidLay9))
	nn.addConnection(FullConnection(hidLay12, h2hidLay9))
	nn.addConnection(FullConnection(hidLay16, h2hidLay9))
	nn.addConnection(FullConnection(hidLay17, h2hidLay9))
	
	nn.addConnection(FullConnection(hidLay12, h2hidLay10))
	nn.addConnection(FullConnection(hidLay13, h2hidLay10))
	nn.addConnection(FullConnection(hidLay17, h2hidLay10))
	nn.addConnection(FullConnection(hidLay18, h2hidLay10))
	
	nn.addConnection(FullConnection(hidLay13, h2hidLay11))
	nn.addConnection(FullConnection(hidLay14, h2hidLay11))
	nn.addConnection(FullConnection(hidLay18, h2hidLay11))
	nn.addConnection(FullConnection(hidLay19, h2hidLay11))
	
	nn.addConnection(FullConnection(hidLay14, h2hidLay12))
	nn.addConnection(FullConnection(hidLay15, h2hidLay12))
	nn.addConnection(FullConnection(hidLay19, h2hidLay12))
	nn.addConnection(FullConnection(hidLay20, h2hidLay12))
	
	nn.addConnection(FullConnection(hidLay16, h2hidLay13))
	nn.addConnection(FullConnection(hidLay17, h2hidLay13))
	nn.addConnection(FullConnection(hidLay21, h2hidLay13))
	nn.addConnection(FullConnection(hidLay22, h2hidLay13))
	
	nn.addConnection(FullConnection(hidLay17, h2hidLay14))
	nn.addConnection(FullConnection(hidLay18, h2hidLay14))
	nn.addConnection(FullConnection(hidLay22, h2hidLay14))
	nn.addConnection(FullConnection(hidLay23, h2hidLay14))
	
	nn.addConnection(FullConnection(hidLay18, h2hidLay15))
	nn.addConnection(FullConnection(hidLay19, h2hidLay15))
	nn.addConnection(FullConnection(hidLay23, h2hidLay15))
	nn.addConnection(FullConnection(hidLay24, h2hidLay15))
	
	nn.addConnection(FullConnection(hidLay19, h2hidLay16))
	nn.addConnection(FullConnection(hidLay20, h2hidLay16))
	nn.addConnection(FullConnection(hidLay24, h2hidLay16))
	nn.addConnection(FullConnection(hidLay25, h2hidLay16))
	
	##connects to 3rd hidden layer
	nn.addConnection(FullConnection(h2hidLay1, h3hidLay1))
	nn.addConnection(FullConnection(h2hidLay2, h3hidLay1))
	nn.addConnection(FullConnection(h2hidLay5, h3hidLay1))
	nn.addConnection(FullConnection(h2hidLay6, h3hidLay1))
	
	nn.addConnection(FullConnection(h2hidLay2, h3hidLay2))
	nn.addConnection(FullConnection(h2hidLay3, h3hidLay2))
	nn.addConnection(FullConnection(h2hidLay6, h3hidLay2))
	nn.addConnection(FullConnection(h2hidLay7, h3hidLay2))
	
	nn.addConnection(FullConnection(h2hidLay3, h3hidLay3))
	nn.addConnection(FullConnection(h2hidLay4, h3hidLay3))
	nn.addConnection(FullConnection(h2hidLay7, h3hidLay3))
	nn.addConnection(FullConnection(h2hidLay8, h3hidLay3))
	
	nn.addConnection(FullConnection(h2hidLay5, h3hidLay4))
	nn.addConnection(FullConnection(h2hidLay6, h3hidLay4))
	nn.addConnection(FullConnection(h2hidLay9, h3hidLay4))
	nn.addConnection(FullConnection(h2hidLay10, h3hidLay4))
	
	nn.addConnection(FullConnection(h2hidLay6, h3hidLay5))
	nn.addConnection(FullConnection(h2hidLay7, h3hidLay5))
	nn.addConnection(FullConnection(h2hidLay10, h3hidLay5))
	nn.addConnection(FullConnection(h2hidLay11, h3hidLay5))
	
	nn.addConnection(FullConnection(h2hidLay7, h3hidLay6))
	nn.addConnection(FullConnection(h2hidLay8, h3hidLay6))
	nn.addConnection(FullConnection(h2hidLay11, h3hidLay6))
	nn.addConnection(FullConnection(h2hidLay12, h3hidLay6))
	
	nn.addConnection(FullConnection(h2hidLay9, h3hidLay7))
	nn.addConnection(FullConnection(h2hidLay10, h3hidLay7))
	nn.addConnection(FullConnection(h2hidLay13, h3hidLay7))
	nn.addConnection(FullConnection(h2hidLay14, h3hidLay7))
	
	nn.addConnection(FullConnection(h2hidLay10, h3hidLay8))
	nn.addConnection(FullConnection(h2hidLay11, h3hidLay8))
	nn.addConnection(FullConnection(h2hidLay14, h3hidLay8))
	nn.addConnection(FullConnection(h2hidLay15, h3hidLay8))
	
	nn.addConnection(FullConnection(h2hidLay11, h3hidLay9))
	nn.addConnection(FullConnection(h2hidLay12, h3hidLay9))
	nn.addConnection(FullConnection(h2hidLay15, h3hidLay9))
	nn.addConnection(FullConnection(h2hidLay16, h3hidLay9))
	
	#connects to hidden layer 4
	nn.addConnection(FullConnection(h3hidLay1, h4hidLay1))
	nn.addConnection(FullConnection(h3hidLay2, h4hidLay1))
	nn.addConnection(FullConnection(h3hidLay4, h4hidLay1))
	nn.addConnection(FullConnection(h3hidLay5, h4hidLay1))
	
	nn.addConnection(FullConnection(h3hidLay2, h4hidLay2))
	nn.addConnection(FullConnection(h3hidLay3, h4hidLay2))
	nn.addConnection(FullConnection(h3hidLay5, h4hidLay2))
	nn.addConnection(FullConnection(h3hidLay6, h4hidLay2))
	
	nn.addConnection(FullConnection(h3hidLay4, h4hidLay3))
	nn.addConnection(FullConnection(h3hidLay5, h4hidLay3))
	nn.addConnection(FullConnection(h3hidLay7, h4hidLay3))
	nn.addConnection(FullConnection(h3hidLay8, h4hidLay3))
	
	nn.addConnection(FullConnection(h3hidLay5, h4hidLay4))
	nn.addConnection(FullConnection(h3hidLay6, h4hidLay4))
	nn.addConnection(FullConnection(h3hidLay8, h4hidLay4))
	nn.addConnection(FullConnection(h3hidLay9, h4hidLay4))

	#connects to outLayer
	nn.addConnection(FullConnection(h4hidLay1,outLayer))
	nn.addConnection(FullConnection(h4hidLay2,outLayer))
	nn.addConnection(FullConnection(h4hidLay3,outLayer))
	nn.addConnection(FullConnection(h4hidLay4,outLayer))
	
	nn.sortModules()

    othello = Othello()
    smartPlayer = SmartPlayer(nn,othello.boardSize)
    greedyPlayer = TacticalPlayer()
    greedyPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]));
    smartPlayer.newGame(othello,greedyPlayer.enemy);

    playGame(othello,greedyPlayer,smartPlayer)
    if othello.getWinner() == greedyPlayer.color:
        outcome = -1
        print "Tactical Player wins over Network Player 7"
        count += 1
        semicount += 1
	
    elif othello.getWinner() == smartPlayer.color:
        outcome = 1
        print "Network Player 7 wins over Tactical Player"		
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
        trainer.trainUntilConvergence(maxEpochs=100)
        NetworkWriter.writeToFile(nn, "othelloNetwork7.xml")
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

