from turtle import Screen, Turtle
from utils import BoardUtils, diceDict, rollDie, ladderDict, getMidpoint, snakeDict
from time import sleep
from random import randint
from sys import argv


class SnakesLadderGame:
    def __init__(self, numCols: int, numRows: int, difficulty: str, darkMode: bool):
        """Initializes the class:

        Arguments:
        numCols -- the number of cols of the board
        numRows -- the number of rows of the board
        difficulty -- easy/medium/hard/impossible the difficulty of the game
        darkMode -- if the user wants to play in dark mode
        """
        self.difficulty = difficulty
        self.darkMode = darkMode

        if "--debug" in argv:
            self.debug = True
        else:
            self.debug = False

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
        self.bullGamesWon = 0
        self.cowGamesWon = 0

        self.initGrid()
        self.numberGrid()
        self.initPlayers()
        self.initSnakeLadder()
        self.initWinTurtle()
        self.initDice()

    def initGrid(self):
        """Create a grid with the number of rows specified in init"""
        self.screen = Screen()
        self.screen.title("Snakes and ladders")
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
        self.cow = Turtle()

        if not self.debug:
            self.bull.up()
            self.cow.up()

        self.bull.goto([15, 15])
        self.bull.shape("./images/bull.gif")

        self.cow.goto([45, 15])
        self.cow.shape("./images/cow.gif")

    def initSnakeLadder(self):
        """Randomly places snakes and ladders on the screen."""

        self.screen.addshape("./images/ladder.gif")
        self.screen.addshape("./images/ladder3.gif")
        self.screen.addshape("./images/snake.gif")
        self.screen.addshape("./images/snake2.gif")
        self.screen.addshape("./images/snake3.gif")

        snakeLadderTurtle = Turtle()

        if not self.debug:
            snakeLadderTurtle.up()

        snakeArray = []
        ladderArray = []

        for i in range(self.numCols):
            # to change difficulty change this probability
            isSnake = randint(1, 2) == 2

            if len(ladderArray) > 2 * len(snakeArray):
                isSnake = True
            elif len(snakeArray) > 2 * len(ladderArray):
                isSnake = False

            if isSnake:
                height = randint(1, 3)
                x1, y1 = i, randint(height, self.numRows - 1)
                x2, y2 = i, y1 - height

                # There is a small change that a snake may be placed starting at the finishing square
                # If this happens, we can move the starting point down by 1
                if (self.numRows % 2 == 1 and x1 == self.numCols - 1 and y1 == self.numRows - 1) or (self.numRows % 2 == 0 and x1 == 0 and y1 == self.numRows - 1):
                    y1 = y1 - 1
                    # If the generated height is 1, then at this point, y2 will equal y1, and there
                    # are no snakes of heigh 0, to fix, we reduce the height of y2 by 1
                    if y1 == y2:
                        y2 = y2 - 1

                snakeArray.append(
                    [
                        self.utils.getPointFromCoordinates([x1, y1]),
                        self.utils.getPointFromCoordinates([x2, y2]),
                    ]
                )
            else:
                height = randint(1, 2)
                x1, y1 = i, randint(0, self.numRows - 1 - height)
                x2, y2 = i, y1 + height
                ladderArray.append(
                    [
                        self.utils.getPointFromCoordinates([x1, y1]),
                        self.utils.getPointFromCoordinates([x2, y2]),
                    ]
                )

            if isSnake:
                snakeLadderTurtle.shape(snakeDict[abs(y2 - y1)])
            else:
                snakeLadderTurtle.shape(ladderDict[abs(y2 - y1)])

            snakeLadderTurtle.goto(
                self.utils.cellMidpoint(
                    self.utils.getPixelCoordinates(
                        getMidpoint([x1, y1], [x2, y2]))
                )
            )
            snakeLadderTurtle.stamp()

            self.snakeArray = snakeArray
            self.ladderArray = ladderArray

        if self.debug:
            print("Snake Array:", snakeArray)
            print("Ladder Array:", ladderArray)

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

    def updateCurrentPlayerGamesWon(self):
        """Increases the number of games won by the current player by 1"""
        if self.currentTurn == "bull":
            self.bullGamesWon += 1
        else:
            self.cowGamesWon += 1

    def getCurrentPlayerPosition(self) -> int:
        """Gets the score of the current player"""
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
            x, y = self.utils.getPixelCoordFromSquare(fromSquare + i + 1)
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
        """Rolls the dice of the current player and handles associated result"""
        userInput = input(
            self.currentTurn.capitalize() + "'s turn. Press enter to roll the dice "
        )
        if userInput == "exit" or userInput == "quit":
            return "game-quit"

        self.animateDiceRoll()

        diceRollScore = rollDie()

        self.updateDiceTurtle(diceRollScore)

        print(self.currentTurn.capitalize(), "rolled a", diceRollScore)

        newPosition = diceRollScore + self.getCurrentPlayerPosition()

        if newPosition > self.maxScore:
            print(
                self.currentTurn,
                "must roll a "
                + str(self.maxScore - self.getCurrentPlayerPosition())
                + " to finish",
            )
        else:
            print(
                self.currentTurn.capitalize(),
                "moved from",
                self.getCurrentPlayerPosition(),
                "to",
                newPosition,
            )

            self.moveCurrentPlayer(
                self.getCurrentPlayerPosition(), newPosition)
            self.setCurrentPlayerPosition(newPosition)
            # Check for snake or ladder
            self.checkForLadder()
            self.checkForSnake()

            if self.getCurrentPlayerPosition() == self.maxScore:
                print(self.currentTurn.capitalize(), "Won!")
                self.winTurtle.showturtle()
                self.updateCurrentPlayerGamesWon()
                self.outputWinStats()
                return "game-complete"

        self.updateCurrentPlayer()
        print("")

    def checkForSnake(self):
        """Checks if the square the current player landed on contains
        the start of a snake
        """
        for x in self.snakeArray:
            if x[0] == self.getCurrentPlayerPosition():
                self.moveCurrentPlayerDirect(x[1])
                self.setCurrentPlayerPosition(x[1])
                print(
                    "Unlucky!,",
                    self.currentTurn,
                    "moved from",
                    str(x[0]),
                    "to",
                    str(x[1]),
                )
                break

    def checkForLadder(self):
        """Checks if the square the current player landed on contains
        the start of a snake
        """
        for x in self.ladderArray:
            if x[0] == self.getCurrentPlayerPosition():
                self.moveCurrentPlayerDirect(x[1])
                self.setCurrentPlayerPosition(x[1])
                print(
                    "Lucky!,",
                    self.currentTurn,
                    "moved from",
                    str(x[0]),
                    "to",
                    str(x[1]),
                )
                break

    def updateCurrentPlayer(self):
        """Toggles between the two players"""
        if self.currentTurn == "bull":
            self.currentTurn = "cow"
        else:
            self.currentTurn = "bull"

    def outputWinStats(self):
        """Outputs both players, and the number of games they have won"""
        print("Bull has won", self.bullGamesWon, "games!")
        print("Cow has won", self.cowGamesWon, "games!")

    def resetGame(self):
        """Moves all players back to the starting square, resets the score, and hides win picture"""
        self.bullScore = 1
        self.cowScore = 1

        self.cow.goto(15, 15)
        self.bull.goto(15, 45)

        self.cow.clear()
        self.bull.clear()

        self.winTurtle.hideturtle()

        self.currentTurn = "bull"


print(
    "This game has been designed for a 5x5 grid, but different sized grids should work. Note the mininum grid height is 4"
)

differentSize = input("Do you want a different sized grid? ").lower()

gridCols, gridRows = 5, 5

if differentSize == "yes":
    gridCols = int(input("How many columns do you want? "))
    gridRows = int(input("How many rows do you want? "))

print("Select your difficulty (easy, medium, difficult or impossible)")
difficulty = input("").lower()

print("Do you want to play in dark mode?")
darkMode = input("").lower()
if darkMode == "yes":
    darkMode = True
else:
    darkMode = False

game = SnakesLadderGame(gridCols, gridRows, difficulty, darkMode)

while True:
    res = game.rollDice()
    if res == "game-quit":
        break
    elif res == "game-complete":
        playAgain = input("Play again?")
        if playAgain.lower() == "no":
            break
        else:
            game.resetGame()
