import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
tim.speed(6)    # somewhat faster speed of pen than normal speed # it can also be tim.speed("normal")

########### Challenge 3 - Draw Shapes ########
colors = ["red","blue","green","orange","black","purple","cyan"]
for i in range(3, 20):
  tim.color(random.choice(colors))
  for j in range(i):
    tim.forward(50)
    angle = 360 / i # angle for each shape
    tim.right(angle)
    
    
# create a hypnotic structure
direction = 2
for i in range(200):
    tim.forward(direction)
    tim.right(90)
    direction += 2
    
screen = Screen()
screen.exitonclick()
