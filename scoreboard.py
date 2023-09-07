from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.write(f"Score: {self.score}", False,
                   "center", ("Courier", 20, "normal"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", False,
                   "center", ("Courier", 20, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.updateScore()
