from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()

def move_forward(): # move forward
    tim.forward(15)
    
def move_backward(): # move backward
    tim.backward(10)
    
def move_anticlockwise(): # turn clockwise
    head = tim.heading()
    tim.setheading(head + 10)  # change the font heading in north direction ie 90
    
def move_clockwise(): # clear the screen
    head = tim.heading()
    tim.setheading(head - 10)

def clear():
    tim.clear()    
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(fun=move_forward, key="w") # move forward
screen.onkey(fun=move_backward, key="s")    # move backward
screen.onkey(fun=move_anticlockwise, key="a")   # turn anti-clockwise
screen.onkey(fun=move_clockwise, key="d")   # turn clockwise
screen.onkey(fun=clear, key="c")    # clear the screen

screen.exitonclick()