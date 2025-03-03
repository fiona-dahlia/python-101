import turtle
import random

def draw_star(x, y, color):    #from Challenge 29
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor(color)
    t.pendown()
    t.hideturtle()
    for i in range(40):
        t.forward(i)
        t.left(144)

window = turtle.Screen()
window.setup(800, 600)
window.title('Example 47')

for count in range(50):
    draw_star(random.randint(-400, 400), random.randint(-300, 300), "yellow")