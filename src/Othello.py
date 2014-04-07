import random
class Othello:
    def __init__(self,boardSize=8):#can pass in any board size
        self.boardSize = boardSize
        self.NO_PIECE = 0         #constant for no piece in square
        self.WHITE_PIECE = 1      #constant for white piece in square
        self.BLACK_PIECE = 2      #constant for black piece in square
        self.WHITE_PLAYER = 1     #constant for black player
        self.BLACK_PLAYER = 2     #constant for white player
        self.NO_PLAYER = 0        #constant for no player
        self.resetGame()

    #resets the games state
    #initializes a board with the initial Othello configuration
    #sets the next player to go to be a random player
    def resetGame(self):
        self.board = []
        for x in xrange(0,self.boardSize):
            self.board.append([])
            for y in xrange(0,self.boardSize):
                if (x > (self.boardSize - 2) / 2 - 1) and (x <= (self.boardSize - 2) / 2 + 1) and (y > (self.boardSize - 2) / 2 - 1) and (y <= (self.boardSize - 2) / 2 + 1):
                    if (x % 2 + y % 2) % 2 == 0:
                        self.board[x].append(self.WHITE_PIECE)
                    else:
                        self.board[x].append(self.BLACK_PIECE)
                else:
                    self.board[x].append(self.NO_PIECE)
        self.winner = self.NO_PLAYER
        self.tieGame = False
        self.nextToGo = random.choice([self.WHITE_PLAYER, self.BLACK_PLAYER])

    #simply gets the piece at a position. -1 signifies error
    def getPieceAtLocation(self,x,y):
        if x < 0 or x >= self.boardSize or y < 0 or y >= self.boardSize:
            return -1
        return self.board[x][y]

    #returns whether or not the game ended
    def isGameOver(self):
        return self.tieGame or self.winner != self.NO_PLAYER

    #returns the winner
    def getWinner(self):
        return self.winner

    #returns if the game ended in a tie game or not
    def isTiedGame(self):
        return self.tieGame

    #returns the player who has the next move
    def whoGoesNext(self):
        return self.nextToGo

    #attempts to make a move into a position for a player
    #returns whether or not the move was allowed
    #if the player isn't the next player to go it will fail
    def makeMove(self,x,y,player):
        if not self.isPossibleMove(x,y,player):
                return False
        if self.nextToGo != player:
            return False
        points = self.getPointsOfChange(x,y,player)
        piece = self.WHITE_PIECE
        if player == self.BLACK_PLAYER:
            piece = self.BLACK_PIECE
        for point in points:
            self.board[point[0]][point[1]] = piece
        if self.nextToGo == self.WHITE_PLAYER:
            self.nextToGo = self.BLACK_PLAYER
        else:
            self.nextToGo = self.WHITE_PLAYER
        self.checkForWinner()
        return True

    #internal method used to check if the game has ended and if so it will set the winner (or tie)
    #this method also passes the play if a player has no moves
    def checkForWinner(self):
        hasMoves = False
        for x in xrange(0,self.boardSize):
            for y in xrange(0,self.boardSize):
                hasMoves = hasMoves or self.isPossibleMove(x,y,self.nextToGo)
        if not hasMoves:
            if self.nextToGo == self.WHITE_PLAYER:
                self.nextToGo = self.BLACK_PLAYER
            else:
                self.nextToGo = self.WHITE_PLAYER
            for x in xrange(0,self.boardSize):
                for y in xrange(0,self.boardSize):
                    hasMoves = hasMoves or self.isPossibleMove(x,y,self.nextToGo)
            if not hasMoves:
                whiteCount = self.getScore(self.WHITE_PLAYER)
                blackCount = self.getScore(self.BLACK_PLAYER)
                if whiteCount == blackCount:
                    self.tieGame = True
                elif whiteCount > blackCount:
                    self.winner = self.WHITE_PLAYER
                else:
                    self.winner = self.BLACK_PLAYER

    #returns the current score (number of tokens on the board) for a player
    def getScore(self,player):
        count = 0
        piece = self.WHITE_PIECE
        if player == self.BLACK_PLAYER:
            piece = self.BLACK_PIECE
        for x in xrange(0,self.boardSize):
            for y in xrange(0,self.boardSize):
                if self.board[x][y] == piece:
                    count += 1
        return count

    #returns whether or not a move is allowed
    def isPossibleMove(self,x,y,player):
        return len(self.getPointsOfChange(x,y,player)) > 0

    #used internally, tells how many points will change if a move is made
    def getPointsOfChange(self,x,y,player):
        if player != self.BLACK_PLAYER and player != self.WHITE_PLAYER:
            return []
        if self.isGameOver():
            return []
        if x < 0 or x >= self.boardSize or y < 0 or y >= self.boardSize:
            return []
        if self.board[x][y] != self.NO_PIECE:
            return []
        points = []
        piece = self.WHITE_PIECE
        enemyPiece = self.BLACK_PIECE
        if player == self.BLACK_PLAYER:
            piece = self.BLACK_PIECE
            enemyPiece = self.WHITE_PIECE

        i = x
        numEnemies = 0
        while True:
            i += 1
            if self.getPieceAtLocation(i,y) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(i,y) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i -= 1
                numEnemies -= 1
                points.append((i,y))

        i = x
        numEnemies = 0
        while True:
            i -= 1
            if self.getPieceAtLocation(i,y) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(i,y) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i += 1
                numEnemies -= 1
                points.append((i,y))


        i = y
        numEnemies = 0
        while True:
            i += 1
            if self.getPieceAtLocation(x,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(x,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i -= 1
                numEnemies -= 1
                points.append((x,i))

        i = y
        numEnemies = 0
        while True:
            i -= 1
            if self.getPieceAtLocation(x,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(x,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i += 1
                numEnemies -= 1
                points.append((x,i))

        i = y
        j = x
        numEnemies = 0
        while True:
            i += 1
            j += 1
            if self.getPieceAtLocation(j,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(j,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i -= 1
                j -= 1
                numEnemies -= 1
                points.append((j,i))

        i = y
        j = x
        numEnemies = 0
        while True:
            i += 1
            j -= 1
            if self.getPieceAtLocation(j,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(j,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i -= 1
                j += 1
                numEnemies -= 1
                points.append((j,i))

        i = y
        j = x
        numEnemies = 0
        while True:
            i -= 1
            j -= 1
            if self.getPieceAtLocation(j,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(j,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i += 1
                j += 1
                numEnemies -= 1
                points.append((j,i))

        i = y
        j = x
        numEnemies = 0
        while True:
            i -= 1
            j += 1
            if self.getPieceAtLocation(j,i) == enemyPiece:
                numEnemies += 1
            elif self.getPieceAtLocation(j,i) == piece:
                break
            else:
                numEnemies = 0
                break
        if numEnemies > 0:
            while numEnemies > -1:
                i += 1
                j -= 1
                numEnemies -= 1
                points.append((j,i))
        return points

    #prints the board out
    def printBoard(self):
        for y in xrange(0,self.boardSize):
            s = ""
            for x in xrange(0,self.boardSize):
                s += str(self.board[x][y])
            print s
