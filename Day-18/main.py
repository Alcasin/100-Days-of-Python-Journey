# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)



import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.up()
tim.hideturtle()
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
start = -250
tim.teleport(start,start)

for up in range(10):
    tim.teleport(-250, start)
    for right in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    start += 50






# import turtle as t
# import random

# from turtle import Turtle, Screen
# from random import randint,choice

# tim = t.Turtle()

# tim.shape("turtle")
# tim.color("red")

# for i in range(50):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# for i in range(3,11):
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)
#     tim.pencolor(randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)


# tim.pensize(10)
# tim.speed("fastest")
# directions = [0,90,180,270]
# for i in range(500):
#     tim.pencolor(randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255)
#     tim.setheading(choice(directions))
#     tim.forward(30)


# t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r,g,b)
#     return rgb_tuple
# directions = [0,90,180,270]
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
#
#

#
# t.colormode(255)
# tim.speed("fastest")
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r,g,b)
#     return rgb_tuple
#
# for i in range(0,360,10):
#     tim.color(random_color())
#     tim.setheading(i)
#     tim.circle(100.0)
#
#
#
#
screen = t.Screen()
screen.exitonclick()