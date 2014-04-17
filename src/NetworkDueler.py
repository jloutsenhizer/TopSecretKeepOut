from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from GreedyPlayer import GreedyPlayer
from Othello import Othello
from Player import playGame
from pybrain.tools.customxml.networkreader import NetworkReader
import random

def runOneTest():
    othello.resetGame()
    player1.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
    player2.newGame(othello,player1.enemy)
    playGame(othello,player1,player2)
    if othello.getWinner() == player1.color:
        return 1.0
    elif othello.getWinner() == player2.color:
        return 0.0
    else:
        return 0.

def vectorSubtract(v1,v2):
    result = []
    for i in xrange(0,len(v1)):
        result.append(v1[i] - v2[i])
    return result

def sum(v):
    accumulator = 0
    for i in xrange(0,len(v)):
        accumulator += v[i]
    return accumulator

def average(v):
    return sum(v) / len(v)

def tTest(name1,results1,name2):
    print("Calculating two tail t-statistics to find average win rate of " + name1 + " against " + name2 + "...")
    difference = results1
    mean = average(difference)
    temp = []
    for i in xrange(0,len(difference)):
        temp.append(pow(difference[i] - mean,2))
    variance = sum(temp) / (len(temp) - 1)
    standardDeviation = pow(variance,0.5)
    lowerBound = mean - tTestInterval * standardDeviation / pow(len(temp),0.5)
    upperBound = mean + tTestInterval * standardDeviation / pow(len(temp),0.5)

    print("95% confident that the win rate lies between:")
    print("[" + str(lowerBound) + "," + str(upperBound) + "]")

othello = Othello()

nn =  NetworkReader.readFrom("othelloNetwork.xml")
player1 = SmartPlayer(nn,othello.boardSize) #change this to some AI you want to look for the win rate of
player2 = GreedyPlayer() #change this to some AI you want to compare against


numTrials = 10000  #change this number to change the number of iterations,
tTestInterval = 1.960 #95% confidence with arbitrarily high degree of freedm (might need to change if numTrials is too low!!!)

dataset = []
for x in xrange(0,numTrials):
    print "Iteration " + str(x+1)
    data = runOneTest()
    dataset.append(data)

tTest("Smart Player Original",dataset,"Random Player") #update these names so output is readable depending on input