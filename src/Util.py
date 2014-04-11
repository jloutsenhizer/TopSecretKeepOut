from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

def saveNetwork(network):
    NetworkWriter.writeToFile(network,"othelloNetwork.xml")

def loadNetwork():
    return NetworkReader.readFrom("othelloNetwork.xml");