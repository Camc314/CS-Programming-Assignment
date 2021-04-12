from random import randint


class BoardUtils:
    """Board utils is a class used for various functions"""

    def __init__(self, numCols: int, numRows: int, gridWidth: int, gridHeight: int):
        """Initializes the class

        Arguments:
        numCols -- number of cols on the board
        numRows -- number of rows on the board
        gridWidth -- width of the board in px
        gridHeight -- height of the board in px
        """
        self.numCols = numCols
        self.numRows = numRows
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

    def getCoordinates(self, squareNumber: int):
        """Gets the correct coordinate for a square on a grid
        Example:
        >>> getCoordinates(12) # 5 rows, 5 cols
        2, 2
        """
        if divmod(squareNumber - 1, self.numCols)[0] % 2 == 0:
            x = divmod(squareNumber - 1, self.numCols)[1]
            y = divmod(squareNumber - 1, self.numCols)[0]
        else:
            x = self.numCols - (divmod(squareNumber - 1, self.numCols)[1]) - 1
            y = divmod(squareNumber - 1, self.numCols)[0]
        return x, y

    def getPixelCoordinates(self, coordinate) -> (int, int):
        """Returns the coordinate of the square in pixels, given a starting coordinate"""
        x = coordinate[0] * self.gridWidth / self.numCols
        y = coordinate[1] * self.gridHeight / self.numRows
        return x, y

    def getPixelCoordFromSquare(self, squareNumber: int) -> (int, int):
        """Returns the coordinate of the square in pixels given a starting square"""
        return self.getPixelCoordinates(self.getCoordinates(squareNumber))

    def getPointFromCoordinates(self, coordinate: (int, int)) -> int:
        """Returns the square number from the input coordinates"""
        score = coordinate[1] * self.numCols

        if coordinate[1] % 2 == 0:
            score = score + coordinate[0] + 1
        else:
            score = score + self.numCols - coordinate[0]

        return score

    def cellMidpoint(self, coordinate: (int, int)) -> (int, int):
        """Gets the center of a cell

        Example: (for a cell size of 100x100)
        >>> cellMidpoint(100,100)
        150, 150
        """
        x, y = coordinate

        x = x + self.gridWidth / (2 * self.numCols)
        y = y + self.gridHeight / (2 * self.numRows)

        return x, y


"""Dictionary contains all dice import paths and the relevant number of points for them"""
diceDict = {
    1: "./images/dice1.gif",
    2: "./images/dice2.gif",
    3: "./images/dice3.gif",
    4: "./images/dice4.gif",
    5: "./images/dice5.gif",
    6: "./images/dice6.gif",
}

"""Dictionary contains all snake import paths and the height for each of them"""
snakeDict = {
    1: "./images/snake2.gif",
    2: "./images/snake.gif",
    3: "./images/snake3.gif",
}

"""Dictionary contains all ladder import paths and the height for each of them"""
ladderDict = {1: "./images/ladder.gif", 2: "./images/ladder3.gif"}


def rollDie() -> int:
    """Mimicks rolling a 6 sided die (returns an int between 1 and 6 (inclusive))

    Example:
    >>> rollDie()
    4
    """
    return randint(1, 6)


def getMidpoint(pointA: (int, int), pointB: (int, int)) -> (int, int):
    """Gets the midpoint between two coordinates

    Example:
    >>> getMidpoint([1,2],[3,4])
    2, 3
    """
    x = (pointA[0] + pointB[0]) / 2
    y = (pointA[1] + pointB[1]) / 2
    return x, y
