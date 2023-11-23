import colorgram
import turtle as t
import random

# paintings = colorgram.extract("damien hirst spots.jpg", 30)

# for paint in paintings:
#     r = paint.rgb.r
#     g = paint.rgb.g
#     b = paint.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)
# print(colors)
colors = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]

t.colormode(255)
tim = t.Turtle()
tim.pu()
tim.hideturtle()
tim.speed(0)

tim.seth(225)
tim.fd(300)
tim.seth(0)

num_of_dots = 101

for dot_count in range(1, num_of_dots):
    tim.dot(20, (random.choice(colors)))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(500)
        tim.seth(0)













































screen = t.Screen()
screen.exitonclick()
