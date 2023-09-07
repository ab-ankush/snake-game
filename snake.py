from turtle import Turtle

position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.x_offset = 0
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for i in position:
            self.addSegment(i)

    def addSegment(self, position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.x_offset -= 20
        self.segments.append(t)

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
