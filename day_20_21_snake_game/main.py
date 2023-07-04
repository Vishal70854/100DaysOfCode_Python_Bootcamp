from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # width and height of screen
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # to perform multiple turtle update positions without glitch in movement

# create Snake object, Food object and Scoreboard object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() # adding controls to screen with keyboard keys
screen.onkey(snake.up, "Up")  #(function(), key)
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

# move snakes as a unit
game_is_on = True
while game_is_on:
  screen.update()  # this lets all snake objects move together
  time.sleep(0.1)

  snake.move()

  # detect collision of snake with food
  # distance method is used to check distance between 2 turtle instances
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # detect collision of snake with wall
  if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
      snake.head.ycor() > 280 or snake.head.ycor() < -280):
    game_is_on = False
    scoreboard.game_over()

  # detect collision with snake tail
  for segment in snake.segments[1:]:  # ignoring head as it is not to be compared
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
      
      
screen.exitonclick()
