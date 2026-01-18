from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_y = -100
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y)
    start_y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()



#  Etch-A-Sketch App
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def reset_screen():
#     tim.reset()
#
# screen.listen()
# screen.onkey(fun=move_forwards , key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=reset_screen, key="c")
# screen.onkey(fun=move_right, key="d")
# screen.onkey(fun=move_left, key="a")
# screen.exitonclick()