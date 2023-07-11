from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xcor, ycor)

    def go_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def go_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)