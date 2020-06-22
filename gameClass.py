
class Game:
    def __init__(self, gameBoard, gameTitle):
        self.gameBoard = gameBoard
        self.playerNum = 0
        self.turnNum = 0
        self.gameTitle = gameTitle

    def reset(self) :
        self.gameBoard[0][0].set(" ")
        self.gameBoard[0][1].set(" ")
        self.gameBoard[0][2].set(" ")

        self.gameBoard[1][0].set(" ")
        self.gameBoard[1][1].set(" ")
        self.gameBoard[1][2].set(" ")

        self.gameBoard[2][0].set(" ")
        self.gameBoard[2][1].set(" ")
        self.gameBoard[2][2].set(" ")

        self.playerNum = 0
        self.turns = 1
        self.gameTitle.set('Player ' + str(self.playerNum + 1) + ' Turn')
        return

    def checkWin(self) :
        #If 5 turns havent passed then the win conditions could not have been met yet
        if (self.turns < 5) :
            return 0

        #Checks rows for win condition
        if (self.gameBoard[0][0].get() == self.gameBoard[0][1].get()  and self.gameBoard[0][1].get() == self.gameBoard[0][2].get() and self.gameBoard[0][0].get() != " ") :
            return 1
        elif (self.gameBoard[1][0].get() == self.gameBoard[1][1].get()  and self.gameBoard[1][1].get() == self.gameBoard[1][2].get() and self.gameBoard[1][0].get() != " ") :
            return 1
        elif (self.gameBoard[2][0].get() == self.gameBoard[2][1].get()  and self.gameBoard[2][1].get() == self.gameBoard[2][2].get() and self.gameBoard[2][0].get() != " ") :
            return 1

        #Checks coloumns for win condition
        if (self.gameBoard[0][0].get() == self.gameBoard[1][0].get()  and self.gameBoard[1][0].get() == self.gameBoard[2][0].get() and self.gameBoard[0][0].get() !=  " ") :
            return 1
        elif (self.gameBoard[0][1].get() == self.gameBoard[1][1].get()  and self.gameBoard[1][1].get() == self.gameBoard[2][1].get() and self.gameBoard[0][1].get() != " ") :
            return 1
        elif (self.gameBoard[0][2].get() == self.gameBoard[1][2].get()  and self.gameBoard[1][2].get() == self.gameBoard[2][2].get() and self.gameBoard[0][2].get() != " ") :
            return 1

        #Checks diagnols for win condition
        if (self.gameBoard[0][0].get() == self.gameBoard[1][1].get() and self.gameBoard[1][1].get() == self.gameBoard[2][2].get() and self.gameBoard[0][0].get() != " ") :
            return 1
        elif (self.gameBoard[2][0].get() == self.gameBoard[1][1].get() and self.gameBoard[1][1].get() == self.gameBoard[0][2].get() and self.gameBoard[2][0].get() != " ") :
            return 1

        #If no conditions have been met yet then we do not have a winner
        return 0

    def setBoard(self, row, col, val) :
        self.gameBoard[row][col].set(val)

    def getPlace(self, row, col) :
        return self.gameBoard[row][col]

    def getPlayer(self) :
        return self.playerNum

    def updateRound(self) :
         self.playerNum = (self.playerNum + 1) % 2
         self.turns += 1
         self.gameTitle.set('Player ' + str(self.playerNum + 1) + ' Turn')