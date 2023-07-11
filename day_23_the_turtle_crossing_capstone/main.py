import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create a player 
player = Player()

# create car object
car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # detect collision of turtle with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # detect if player reaches other side of screen
    if player.is_at_finish_line():
        player.go_to_start()    # move turtle to original position
        car_manager.level_up()  # increase the speed of cars
        scoreboard.increase_level()

screen.exitonclick()
