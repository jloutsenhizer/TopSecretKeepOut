from pybrain.structure import FeedForwardNetwork
from pybrain.datasets import SupervisedDataSet

'''
	The "Smart"Player class uses the current network to pick moves and remembers those moves.
	At the end of the game, the remembered moves' weights are updated based on the outcome


	Note:  I'd like to draw your attention to the gameOver method.  I made some design choices here about the update rules; we should discuss any disagreements.
'''
class SmartPlayer:
	def __init__(self, network, boardSize, color):
		self.boardSize = boardSize
		self.n = network
		self.data = []
		self.ds = SupervisedDataSet(boardSize * boardSize, 1)
		self.color = color
		if color == 1:
			self.enemy = 2
		else:
			self.enemy = 1

	def newGame(self, network, color):
		self.n = network
		slef.data = []
		self.ds.clear()
		self.color = color
		if color == 1:
			self.enemy = 2
		else:
			self.enemy = 1

	def gameOver(self, outcome): #returns a dataset updated based on the argument outcome (-1 loss, 0 draw, 1 win)
		'''
	I wasn't completely sure what we should use for the update rules here
	I chose the win/loss updates so that the values would increase/decrease respectively while remaining between 0 and 1 (should we instead allow them to increase without bound?)
	For the draw I just fed the same value back in; this feels pointless but I can't think of an alternative
		'''		

		if outcome == 0:
			for t in self.data:
				ds.addSample(t[0], t[1])
		elif outcome == 1:
			for t in self.data:
				ds.addSample(t[0], t[1] ** (0.5))
		else:
			for t in self.data:
				ds.addSample(t[0], t[1] ** 2)

		return ds

	def getMoves(self, board): #returns a list of (x, y) pairs that are the viable moves for the argument board configuration
		'''
	I didn't write this method yet because I thought Emily may be writing/have written something very similar.  I'll keep working on it, and if I finish I will update
		'''
		return [(0,0)]

	def getMove(self, board):  #returns the network's choice for "best" move (in the form [x, y]) for the argument 2d array board
		max = 0
		maxMove = []
		maxBoard = []
		curBoard = []
		for x in xrange(0, self.boardSize):
			for y in xrange(0, self.boardSize):
				curBoard.append(board[x][y])
		
		for move in getMoves(board):
			switch = []
			nextBoard = list(curBoard)
			x = move[0]
			y = move[1]
	
			i = x
			while True:
				i += 1
				if i >= self.boardSize:
					switch = []
					break
				if board[i][y] == self.enemy:
					switch.append((i, y))
				elif board[i][y] == self.color:
					break
				else:
					switch = []
					break
			
			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color

			


			switch = []
			i = x
			while True:
				i -= 1
				if i < 0:
					switch = []
					break
				if board[i][y] == self.enemy:
					switch.append((i, y))
				elif board[i][y] == self.color:
					break
				else:
					switch = []
					break
	
			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color



			switch = []
			i = y
			while True:
				i += 1
				if i >= self.boardSize:
					switch = []
					break
				if board[x][i] == self.enemy:
					switch.append((x, i))
				elif board[x][i] == self.color:
					break
				else:
					switch = []
					break
		
			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color



			switch = []
			i = y
			while True:
				i -= 1
				if i < 0:
					switch = []
					break
				if board[x][i] == self.enemy:
					switch.append((x, i))
				elif board[x][i] == self.color:
					break
				else:
					switch = []
					break

			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color

	

			switch = []
			j = y
			i = x
			while True:
				i += 1
				j += 1
				if i >= self.boardSize or j >= self.boardSize:
					switch = []
					break
				if board[i][j] == self.enemy:
					switch.append((i, j))
				elif board[i][j] == self.color:
					break
				else:
					switch = []
					break

			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color

			

			switch = []
			j = y
			i = x
			while True:
				i += 1
				j -= 1
				if i >= self.boardSize or j < 0:
					switch = []
					break
				if board[i][j] == self.enemy:
					switch.append((i, j))
				elif board[i][j] == self.color:
					break
				else:
					switch = []
					break

			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color

			

			switch = []
			j = y
			i = x
			while True:
				i -= 1
				j += 1
				if i < 0 or j >= self.boardsize:
					switch = []
					break
				if board[i][j] == self.enemy:
					switch.append((i, j))
				elif board[i][j] == self.color:
					break
				else:
					switch = []
					break

			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color


			switch = []
			j = y
			i = x
			while True:
				i -= 1
				j -= 1
				if i < 0 or j < 0:
					switch = []
					break
				if board[i][j] == self.enemy:
					switch.append((i, j))
				elif board[i][j] == self.color:
					break
				else:
					switch = []
					break

			for t in switch:
				nextBoard[(t[0] * self.boardSize) + t[1]] = self.color
	
			pred = n.activate(nextBoard)

			if pred > max:
				max = pred
				maxMove = [x, y]
				maxBoard = list(nextBoard)
		
		self.data.append((maxBoard, pred))
		
		return maxMove

