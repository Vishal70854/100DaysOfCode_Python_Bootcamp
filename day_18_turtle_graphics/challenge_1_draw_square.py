from turtle import Turtle, Screen

turtle = Turtle()   # create an instance of Turtle class 
turtle.shape("turtle")  # create a new shape for the turtle
turtle.color("red")     # set the color of the turtle



for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

screen = Screen()   
screen.exitonclick()    # screen will exit when we click on the screen.