from turtle import Screen, Turtle
from utils import BoardUtils, diceDict, rollDie
from time import sleep


class SnakesLadderGame:
    def __init__(self, numCols: int, numRows: int, difficulty="medium"):
        self.difficulty = difficulty

        self.numCols = numCols
        self.numRows = numRows
        self.gridHeight = 375
        self.gridWidth = 375

        self.maxScore = self.numCols * self.numRows

        self.utils = BoardUtils(
            self.numCols, self.numRows, self.gridWidth, self.gridHeight
        )

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
                [(i * (self.gridWidth / self.numRows)), self.gridHeight])

    def numberGrid(self):
        """Labels numbers for all squares on the grid"""
        numberTurtle = Turtle()
        numberTurtle.hideturtle()
        numberTurtle.up()

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


print("This game has been designed for a 5x5 grid, but different sized grids should work.")
differentSize = input("Do you want a different sized grid? ")

gridCols, gridRows = 5, 5

if differentSize.lower() == "yes":
    gridCols = int(input("How many columns do you want? "))
    gridRows = int(input("How many rows do you want? "))

print("Select your difficulty (easy, medium, difficult or impossible)")
difficulty = input("")

a = SnakesLadderGame(gridCols, gridRows, difficulty)
