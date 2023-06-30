from turtle import Turtle, Screen
import colorgram
import random

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#     r, g, b = color.rgb # unpacking values
#     color_list.append((r, g, b))
# print(color_list)


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# Setting the screen color-mode
scr = Screen()
scr.colormode(255)

color_list = [(235, 232, 227), (230, 233, 239), (239, 231, 235), (227, 236, 230),
              (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50),
              (132, 28, 53), (219, 205, 120), (29, 40, 65),
              (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158)]

tim.setheading(225)  # somewhere between south-west direction
tim.forward(300)
tim.setheading(0)   # east direction

num_of_dots = 100
for dot in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
#
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

scr.exitonclick()
