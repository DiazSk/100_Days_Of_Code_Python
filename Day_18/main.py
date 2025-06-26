import colorgram

rgb_colors = []
colors = colorgram.extract('Day18/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Extracted colors from the image
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

tim.penup()
tim.hideturtle()
tim.setposition(-250, -200)
tim.pendown()

num_rows = 10
num_cols = 10
current_row = 0

while current_row < num_rows:
    for _ in range(num_cols):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.setposition(-250, -200 + (current_row + 1) * 50)
    current_row += 1
    

screen = t.Screen()
screen.exitonclick()