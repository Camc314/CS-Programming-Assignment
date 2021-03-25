class BoardUtils:
    def __init__(self, numCols: int, numRows: int, gridWidth: int, gridHeight: int):
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


diceDict = {
    1: "./images/dice1.gif",
    2: "./images/dice2.gif",
    3: "./images/dice3.gif",
    4: "./images/dice4.gif",
    5: "./images/dice5.gif",
    6: "./images/dice6.gif",
}
