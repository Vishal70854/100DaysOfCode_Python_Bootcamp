import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270] # [east, north, south, west]
tim.speed(0)    # fastest speed of pen # it can also be tim.speed("fastest")
tim.pensize(10)

for _ in range(200):    
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
