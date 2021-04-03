from turtle import Screen, Turtle
from utils import BoardUtils, diceDict, rollDie
from time import sleep


class SnakesLadderGame:
    def __init__(self, numCols: int, numRows: int, difficulty: str, darkMode: bool):
        self.difficulty = difficulty
        self.darkMode = darkMode

        self.numCols = numCols
        self.numRows = numRows
        self.gridHeight = 375
        self.gridWidth = 375

        self.maxScore = self.numCols * self.numRows

        self.utils = BoardUtils(
            self.numCols, self.numRows, self.gridWidth, self.gridHeight
        )

        self.currentTurn = "bull"
        self.bullScore = 1
        self.cowScore = 1

        self.initGrid()
        self.numberGrid()
        self.initPlayers()
        self.initWinTurtle()
        self.initDice()

    def initGrid(self):
        """Create a grid"""
        self.screen = Screen()
        self.screen.setworldcoordinates(-100, -100, 400, 400)
        turtle = Turtle()
        turtle.speed(10)

        if self.darkMode:
            self.screen.bgcolor("black")
            turtle.color("white")

        turtle.hideturtle()
        for i in range(self.numRows + 1):
            turtle.penup()
            turtle.goto([0, (i * (self.gridHeight / self.numRows))])
            turtle.pendown()
            turtle.goto(
                [self.gridWidth, (i * (self.gridHeight / self.numRows))])

        turtle.setheading(0)

        for i in range(self.numCols + 1):
            turtle.penup()
            turtle.goto([(i * (self.gridWidth / self.numCols)), 0])
            turtle.pendown()
            turtle.goto(
                [(i * (self.gridWidth / self.numCols)), self.gridHeight])

    def numberGrid(self):
        """Labels numbers for all squares on the grid"""
        numberTurtle = Turtle()
        numberTurtle.hideturtle()
        numberTurtle.up()

        if self.darkMode:
            numberTurtle.color("white")

        for i in range(self.maxScore):
            x, y = self.utils.getCoordinates(i + 1)
            y = y + 1
            x, y = self.utils.getPixelCoordinates([x, y])

            numberTurtle.goto(x + 10, y - 20)
            numberTurtle.write(str(i + 1))

    def initPlayers(self):
        """Creates turtles for the bull/cow and places them on the screen"""
        self.screen.addshape("./images/bull.gif")
        self.screen.addshape("./images/cow.gif")

        self.bull = Turtle()
        self.bull.goto([15, 15])
        self.bull.shape("./images/bull.gif")

        self.cow = Turtle()
        self.cow.goto([45, 15])
        self.cow.shape("./images/cow.gif")

    def initDice(self):
        """Initializes the turtle containing the dice"""

        for i in diceDict:
            self.screen.addshape(diceDict[i])

        self.dice = Turtle()
        self.dice.penup()
        self.dice.goto(-50, 200)
        self.dice.shape(diceDict[1])

    def initWinTurtle(self):
        """Initializes the turtle containing the win gif"""
        self.screen.addshape("./images/win.gif")
        self.winTurtle = Turtle()
        self.winTurtle.up()
        self.winTurtle.hideturtle()
        self.winTurtle.goto(150, 150)
        self.winTurtle.shape("./images/win.gif")

    def animateDiceRoll(self):
        """Outputs 6 random dice images to the screen to mimic rolling a die"""
        for i in range(6):
            self.dice.shape(diceDict[rollDie()])
            sleep(0.05)

    def updateDiceTurtle(self, newDiceRoll: int):
        """Updates the current image of the dice"""
        self.dice.shape(diceDict[newDiceRoll])

    def getCurrentPlayer(self) -> Turtle:
        """Returns the Turtle of the current player"""
        if self.currentTurn == "bull":
            return self.bull
        return self.cow

    def getCurrentPlayerPosition(self) -> int:
        if self.currentTurn == "bull":
            return self.bullScore
        return self.cowScore

    def setCurrentPlayerPosition(self, newScore: int):
        """Sets the score of the current player"""
        if self.currentTurn == "bull":
            self.bullScore = newScore
        else:
            self.cowScore = newScore

    def moveCurrentPlayer(self, fromSquare: int, toSquare: int):
        """Moves a player sequentally from square to square"""
        playerToMove = self.getCurrentPlayer()

        for i in range(toSquare - fromSquare):
            x, y = self.utils.getPixelCoordFromSquare(fromSquare + i+1)
            if self.currentTurn == "bull":
                x = x + 15
            else:
                x = x + 45
            playerToMove.goto(x, y + 15)

    def moveCurrentPlayerDirect(self, toSquare: int):
        """Moves the current player directly from their current square to the new square"""
        playerToMove = self.getCurrentPlayer()

        x, y = self.utils.getPixelCoordFromSquare(toSquare)
        if self.currentTurn == "bull":
            x = x + 15
        else:
            x = x + 45

        playerToMove.goto(x, y + 15)

    def rollDice(self):
        userInput = input(self.currentTurn.capitalize() +
                          "'s turn. Press enter to roll the dice ")
        if userInput == 'exit' or userInput == 'quit':
            return 'game-quit'

        self.animateDiceRoll()

        diceRollScore = rollDie()

        self.updateDiceTurtle(diceRollScore)

        print(self.currentTurn.capitalize(), "rolled a", diceRollScore)

        newPosition = diceRollScore + self.getCurrentPlayerPosition()

        if newPosition > self.maxScore:
            print(
                self.currentTurn, "must roll a "
                + str(self.maxScore - self.getCurrentPlayerPosition())
                + " to finish"
            )
        else:
            print(self.currentTurn.capitalize(), "moved from",
                  self.getCurrentPlayerPosition(), "to", newPosition)

            self.moveCurrentPlayer(
                self.getCurrentPlayerPosition(), newPosition)
            self.setCurrentPlayerPosition(newPosition)
            # Check for snake or ladder

            if self.getCurrentPlayerPosition() == self.maxScore:
                print(self.currentTurn.capitalize(), "Won!")
                self.winTurtle.showturtle()
                return "game-complete"

        self.updateCurrentPlayer()
        print("")

    def updateCurrentPlayer(self):
        if self.currentTurn == "bull":
            self.currentTurn = "cow"
        else:
            self.currentTurn = "bull"

    def resetGame(self):
        self.bullScore = 1
        self.cowScore = 1

        self.cow.goto(15, 15)
        self.bull.goto(15, 45)

        self.cow.clear()
        self.bull.clear()

        self.winTurtle.hideturtle()

        self.currentTurn = "bull"


print(
    "This game has been designed for a 5x5 grid, but different sized grids should work."
)

differentSize = input("Do you want a different sized grid? ")

gridCols, gridRows = 5, 5

if differentSize.lower() == "yes":
    gridCols = int(input("How many columns do you want? "))
    gridRows = int(input("How many rows do you want? "))

print("Select your difficulty (easy, medium, difficult or impossible)")
difficulty = input("")

print("Do you want to play in dark mode?")
darkMode = input("")
if darkMode.lower() == 'yes':
    darkMode = True
else:
    darkMode = False

game = SnakesLadderGame(gridCols, gridRows, difficulty, darkMode)

while True:
    res = game.rollDice()
    if res == 'game-quit':
        break
    elif res == "game-complete":
        playAgain = input("Play again?")
        if playAgain.lower() == "no":
            break
        else:
            game.resetGame()
