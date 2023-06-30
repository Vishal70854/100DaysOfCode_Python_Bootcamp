from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.speed("fastest")

### challenge 5 draw a spirograph

colors = ["brown", "black","cyan","red","green","yellow","orange","violet","purple"]

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(50) # radius of circle
        tim.setheading(tim.heading() + size_of_gap)
        # it will also be created using left method specifying an angle
        # tim.left(10)    # each time circle pointer move to 10 degree left

draw_spirograph(5)  # space between each circle

screen.exitonclick()