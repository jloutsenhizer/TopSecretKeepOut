from SmartPlayer import SmartPlayer
from RandomPlayer import RandomPlayer
from GreedyPlayer import GreedyPlayer
from Othello import Othello
from Player import playGame
from pybrain.tools.customxml.networkreader import NetworkReader
import random

def runOneTest():
    rvrP1Wins = 0
    rvrP2Wins = 0
    rvrTies = 0
    gvrP1Wins = 0
    gvrP2Wins = 0
    gvrTies = 0
    nvrP1Wins = 0
    nvrP2Wins = 0
    nvrTies = 0

    for x in xrange(0,1):#run 100 gamess
        #print "Iteration " + str(x+1)
        #print "Random vs Random"
        othello.resetGame()
        player1.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
        opponentPlayer.newGame(othello,player1.enemy)
        playGame(othello,player1,opponentPlayer)
        if othello.getWinner() == player1.color:
            rvrP1Wins += 1
            #print "Random Player 1 is vicotorious! Glory to the RNG!"
        elif othello.getWinner() == opponentPlayer.color:
            rvrP2Wins += 1
            #print "Random Player 2 is victorious! Glory to the RNG!"
        else:
            rvrTies += 1
            #print "Tie game! :("

        othello.resetGame()
        player2.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
        opponentPlayer.newGame(othello,player2.enemy)
        playGame(othello,player2,opponentPlayer)
        if othello.getWinner() == player2.color:
            gvrP1Wins += 1
            #print "Random Player 1 is vicotorious! Glory to the RNG!"
        elif othello.getWinner() == opponentPlayer.color:
            gvrP2Wins += 1
            #print "Random Player 2 is victorious! Glory to the RNG!"
        else:
            gvrTies += 1
            #print "Tie game! :("

        othello.resetGame()
        player3.newGame(othello,random.choice([othello.WHITE_PLAYER,othello.BLACK_PLAYER]))
        opponentPlayer.newGame(othello,player3.enemy)
        playGame(othello,player3,opponentPlayer)
        if othello.getWinner() == player3.color:
            nvrP1Wins += 1
            #print "Smart Player is victorious! Glory to the Machine Brains!"
        elif othello.getWinner() == opponentPlayer.color:
            nvrP2Wins += 1
            #print "Random Player is victorious!"
        else:
            nvrTies += 1
            #print "Tie game! D:"
    #print "Random vs Random win rate: " + str(rvrP1Wins / float(rvrP1Wins + rvrP2Wins + rvrTies))
    #print "Network vs Random win rate: " + str(nvrP1Wins / float(nvrP1Wins + nvrP2Wins + nvrTies))
    return (rvrP1Wins / float(rvrP1Wins + rvrP2Wins + rvrTies),gvrP1Wins / float(gvrP1Wins + gvrP2Wins + gvrTies),nvrP1Wins / float(nvrP1Wins + nvrP2Wins + nvrTies))

tTestInterval = 1.960

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

def tTest(name1,results1,name2,results2):
    print("Calculating two tail t-statistics to find difference between " + name1 + " and " + name2 + "...")
    difference = vectorSubtract(results1,results2)
    mean = average(difference)
    temp = []
    for i in xrange(0,len(difference)):
        temp.append(pow(difference[i] - mean,2))
    variance = sum(temp) / (len(temp) - 1)
    standardDeviation = pow(variance,0.5)
    lowerBound = mean - tTestInterval * standardDeviation / pow(len(temp),0.5)
    upperBound = mean + tTestInterval * standardDeviation / pow(len(temp),0.5)

    print("95% confident that the difference between the two algorithm's accuracy lies between:")
    print("[" + str(lowerBound) + "," + str(upperBound) + "]")

    if (0 >= lowerBound) & (0 <= upperBound):
        print("0 is inside the interval, therefore we can't tell if there's a difference between the two algorithms with 95% confidence")
    elif lowerBound < 0:
        print("0 is outside the interval, therefore we can conclude with 95% confidence that " + name2 + " performs better than " + name1 + " on this dataset.")
    else:
        print("0 is outside the interval, therefore we can conclude with 95% confidence that " + name1 + " performs better than " + name2 + " on this dataset.")



opponentPlayer = RandomPlayer()  #change this to change the opponent to be testing against

nn = NetworkReader.readFrom("othelloNetwork1.xml")
player1 = SmartPlayer(nn,8)
nn = NetworkReader.readFrom("othelloNetwork2.xml")
player2 = SmartPlayer(nn,8)
nn = NetworkReader.readFrom("othelloNetwork3.xml")
player3 = SmartPlayer(nn,8)
othello = Othello()


numTrials = 10000  #change this number to change the number of iterations,

data1 = []
data2 = []
data3 = []
for x in xrange(0,numTrials):
    print "Iteration " + str(x+1)
    data = runOneTest()
    data1.append(data[0])
    data2.append(data[1])
    data3.append(data[2])

tTest("NN1 Player",data1,"NN2 Player",data2)
print ""
tTest("NN2 Player",data2,"NN3 Player",data3)
print ""
tTest("NN1 Player",data1,"NN3 Player",data3)
