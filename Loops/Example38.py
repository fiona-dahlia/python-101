import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("Example 38")

t = turtle.Turtle()
t.speed("fast")
t.pensize(1)
t.pencolor("blue")

colors = ("red", "blue", "green", "purple")

num_sides = 4

for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.forward(x)
    t.left(360 / num_sides + 2)