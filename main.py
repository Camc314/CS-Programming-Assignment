from turtle import Screen, Turtle


class SnakesLadderGame:
    def __init__(self):
        self.numCols = 5
        self.numRows = 5
        self.gridHeight = 375
        self.gridWidth = 375

        self.initGrid()

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


SnakesLadderGame()
