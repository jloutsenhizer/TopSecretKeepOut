#Mario Minyon
#CS 1675
#HW 3
from pybrain.datasets            import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from Othello import Othello
import random



#sets a ClassificationDataSet with 16 inputs and 10 outputs
ds = ClassificationDataSet(192,64,nb_classes=64)
ds = GETDATAFROMSMARTPLAYER()

#create network with no hidden layers
nn = FeedForwardNetwork()
inLayer = LinearLayer(192)
outLayer = SoftmaxLayer(64)
nn.addInputModule(inLayer)
nn.addOutputModule(outLayer)
nn.addConnection(FullConnection(inLayer, outLayer))
nn.sortModules()

othello = Othello()
smartPlayer = SmartPlayer(nn,othello.boardSize)
randomPlayer = RandomPlayer()
randomPlayer.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]));
smartPlayer.newGame(othello,randomPlayer.enemy);

while not othello.isGameOver():
	if (othello.whoGoesNext() == randomPlayer.color):
		move = randomPlayer.getMove()
		othello.makeMove(move[0],move[1],randomPlayer.color)
	else:
		move = smartPlayer.getMove()
		othello.makeMove(move[0],move[1],smartPlayer.color)
if othello.getWinner() == randomPlayer.color:
	outcome = -1
else if othello.getWinner() == smartPlayer.color:
	outcome = 1
else
	outcome = 0

ds = smartPlayer.gameOver(outcome)
if (ds != None):
	trainer = BackpropTrainer(nn, dataset=ds)
	trainer.trainUntilConvergence(maxEpochs=100)
