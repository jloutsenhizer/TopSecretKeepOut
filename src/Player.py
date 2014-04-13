
def playGame(othello,player1,player2):
	while not othello.isGameOver():
		if (othello.whoGoesNext() == player1.color):
			move = player1.getMove()
			othello.makeMove(move[0],move[1],player1.color)
		else:
			move = player2.getMove()
			othello.makeMove(move[0],move[1],player2.color)
