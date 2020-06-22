from tkinter import *
from tkinter import messagebox
from gameClass import *

def clicked(row, col, game) :
    
    if (game.getPlayer() == 1 and game.getPlace(row, col).get() == " ") :
        game.setBoard(row, col, "O")
    elif (game.getPlayer() == 0 and game.getPlace(row, col).get() == " ") :
        game.setBoard(row, col, "X")
    else :
        return

    if(game.checkWin()) :
        messagebox.showinfo(title= 'Winner', message= "Winner is Player " + str(game.getPlayer() + 1))
        game.reset()
    else :
        game.updateRound()
    return

root = Tk()
root.geometry("1000x1000")
root.title("Tik Tak Toe")

displayTxt = StringVar()
gameLabel =  Label(textvariable = displayTxt)
gameLabel.pack()

gameFrame = Frame(root, height = 1000, width = 1000)
gameFrame.pack()

 

gameBoard = [[StringVar(), StringVar(), StringVar()], [StringVar(), StringVar(), StringVar()], [StringVar(), StringVar(), StringVar()]]
myGame = Game(gameBoard, displayTxt)
myGame.reset()


resetButton = Button(text = "RESET", command = lambda : myGame.reset())
resetButton.pack()

row1 = Frame(gameFrame)
row2 = Frame(gameFrame)
row3 = Frame(gameFrame)

row1.pack()
row2.pack()
row3.pack()

topLeft = Button(row1, textvariable = myGame.getPlace(0, 0), command =  lambda : clicked(0, 0, myGame))
topMiddle = Button(row1, textvariable = myGame.getPlace(0, 1), command =  lambda : clicked(0, 1, myGame))
topRight = Button(row1, textvariable = myGame.getPlace(0, 2), command =  lambda : clicked(0, 2, myGame))


topLeft.pack(side = LEFT)
topMiddle.pack(side = LEFT)
topRight.pack(side = LEFT)

middleLeft = Button(row2, textvariable = myGame.getPlace(1, 0), command =  lambda : clicked(1, 0, myGame))
middleMiddle = Button(row2, textvariable = myGame.getPlace(1, 1), command =  lambda : clicked(1, 1, myGame))
middleRight = Button(row2, textvariable = myGame.getPlace(1, 2), command =  lambda : clicked(1, 2, myGame))


middleLeft.pack(side = LEFT)
middleMiddle.pack(side = LEFT)
middleRight.pack(side = LEFT)

bottomLeft = Button(row3, textvariable = myGame.getPlace(2, 0), command =  lambda : clicked(2, 0, myGame))
bottomMiddle = Button(row3, textvariable = myGame.getPlace(2, 1), command =  lambda : clicked(2, 1, myGame))
bottomRight = Button(row3, textvariable = myGame.getPlace(2, 2), command =  lambda : clicked(2, 2, myGame))


bottomLeft.pack(side = LEFT)
bottomMiddle.pack(side = LEFT)
bottomRight.pack(side = LEFT)



root.mainloop()