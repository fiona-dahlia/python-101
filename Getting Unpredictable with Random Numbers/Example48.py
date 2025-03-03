import turtle
import random

window = turtle.Screen()
window.setup(800, 600)
window.title('Example 48')

t = turtle.Turtle()
t.speed("fastest")

colors = ("red", "blue", "orange", "purple", "green")

random.seed(5)

for x in range(100):
    t.pencolor(random.choice(colors))
    t.pensize(random.randint(1, 10))
    t.left(random.randint(0, 360))
    t.forward(random.randint(10, 50))