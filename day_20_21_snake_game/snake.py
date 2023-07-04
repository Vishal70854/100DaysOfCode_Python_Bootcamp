from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # constants in Python. Snake case
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
  # create snake from 3 turtle object aligned on x-axis
  def __init__(self):
    # create snake from turtle objects
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  # create snake from turtle objects
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)
      
  def add_segment(self, position):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())

  # move the snake
  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)

    self.head.forward(MOVE_DISTANCE)    # move the head of snake forward

  # move snake up
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  # move snake left
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  # move snake down
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  # move snake right
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
