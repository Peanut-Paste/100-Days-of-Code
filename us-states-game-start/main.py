import pandas
import turtle
from map_write import MapWrite


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
map_write = MapWrite()
states = pandas.read_csv("50_states.csv")
states_list = states.state.tolist()
guessed_states = []


while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        row = states[states.state == answer_state]
        map_write.write(answer_state, int(row["x"]), int(row["y"]))







