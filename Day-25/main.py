import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = data.state.to_list()
guessed_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct",
                                    prompt="State name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t_data = data[data.state == answer_state]
        writer.goto(int(t_data.x.item()), int(t_data.y.item()))
        writer.write(answer_state)

# states_to_learn = list(set(all_states) - set(guessed_states))
#
# data_dict = {
#     "states": states_to_learn
# }
# learn_data = pandas.DataFrame(data_dict)
# learn_data.to_csv("states_to_learn.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

