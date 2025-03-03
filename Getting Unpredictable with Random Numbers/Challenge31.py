import turtle
import random

def draw_star(x, y, color):
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(5)
    t.pencolor(color)
    t.pendown()
    t.hideturtle()
    for x in range(40):
        t.forward(x)
        t.left(144)

window = turtle.Screen()
window.setup(800, 600)
window.title('Example 47')

colors = ("red", "blue", "orange", "purple", "green")

for count in range(50):
    draw_star(random.randint(-400, 400), random.randint(-300,300), random.choice(colors))