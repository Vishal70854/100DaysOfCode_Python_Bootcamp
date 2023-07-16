import pandas
from turtle import Turtle, Screen
FONT = ("Courier", 12, "normal")

turtle = Turtle()
screen = Screen()
screen.title("U.S.STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()   # convert a series column into a list

# print(answer_state)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", 
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        remaining_states = []   # get all remaining states not typed by user
        for state_name in all_states:
            if state_name not in guessed_states:
                remaining_states.append(state_name)
        print(remaining_states)
                
        state_dict = {"states": remaining_states}   # create a dictionary with column name states
        state_list = pandas.DataFrame(state_dict)   # create table in csv format in python
        state_list.to_csv("states_to_learn.csv")    # transfer all data in a csv file mentioned
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv



