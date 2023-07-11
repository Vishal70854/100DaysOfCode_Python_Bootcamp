from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)# turn off the animation then we have to manually update the tracer for smooth transitions


# create a paddle object
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# create a Ball object
ball = Ball()

# create scoreboard object
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # manually update the tracer
    ball.move()
    
    # detect collision of ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce back the ball
        ball.bounce_y()
    
    # detect collision of ball with right and left paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or 
        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
            ball.bounce_x()
            
    # detect if ball misses right paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
        
    # detect if ball misses left paddle
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
