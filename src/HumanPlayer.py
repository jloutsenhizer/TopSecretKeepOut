class HumanPlayer:
    def newGame(self, game, color):
        self.color = color
        self.game = game;
        if color == self.game.WHITE_PLAYER:
            print "You are the white player"
            self.enemy = self.game.BLACK_PLAYER
        else:
            print "You are the black player"
            self.enemy = self.game.WHITE_PLAYER

    def getMove(self):  #returns the network's choice for "best" move
        print "Current Board:"
        self.game.printBoard()
        print ""
        move = None
        while move not in self.game.getAllPossibleMoves(self.color):
            if move != None:
                print "invalid move!"
            move = raw_input("Enter Your Move x,y: ")
            move = move.split(",")
            move = (int(move[0])-1,int(move[1])-1)#makes it so indexing starts at 1 instead of 0

        return move