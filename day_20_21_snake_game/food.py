from turtle import Turtle
import random


class Food(Turtle):  # inherit Turtle class

  def __init__(self):
    super().__init__()  # initialization of constuctor of Turtle class
    self.shape("turtle")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)