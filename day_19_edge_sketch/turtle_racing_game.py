from turtle import Turtle, Screen
import random

is_race_on = False
scr = Screen()
scr.setup(width=500, height=400)
user_color = scr.textinput(title="Turtle racing game", prompt="Which turtle will win? Enter a color :")
colors = ["red", "green", "blue","yellow","brown", "black"]

if user_color:
    is_race_on = True
    
y_coordinate = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate[i])
    all_turtles.append(new_turtle)

winner = None
while is_race_on:
    
    for turtle in all_turtles:
        if int(turtle.xcor()) > 230:    #since turtle size is 40 by 40 so subtract 250- (40/2)
            winner = turtle.pencolor()
            if winner == user_color:
                print(f" You've won. The winner turtle is {winner}")
            else:
                print(f"You've lost. The winner turtle is {winner}")
            
            is_race_on = False
            break
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        
scr.exitonclick()