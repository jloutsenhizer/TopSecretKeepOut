#Mario Minyon
#CS 1675
#HW 3
from pybrain.datasets            import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from SmartPlayer import SmartPlayer

#sets a ClassificationDataSet with 16 inputs and 10 outputs
ds = ClassificationDataSet(192,64,nb_classes=64)
ds = GETDATAFROMSMARTPLAYER()

tstdata, trndata = ds.splitWithProportion( 0.25 )

trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )


#create network with no hidden layers
nn = FeedForwardNetwork()
inLayer = LinearLayer(192)
outLayer = SoftmaxLayer(64)
nn.addInputModule(inLayer)
nn.addOutputModule(outLayer)
nn.addConnection(FullConnection(inLayer, outLayer))
nn.sortModules()

trainer = BackpropTrainer(n, dataset=trndata)
trainer.trainUntilConvergence(maxEpochs=100)
