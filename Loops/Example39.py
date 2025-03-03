import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("Example 39")

t = turtle.Turtle()
t.speed("fast")
t.pensize(5)
colors = ("red", "blue", "green", "orange", "purple", "yellow", "yellow", "yellow")

for x in range(0, 180, 1):
    t.goto(0, 0)
    t.setheading(2 * x)
    t.pencolor(colors[x % len(colors)])
    t.forward(200)
    t.left(30)
    t.forward(25)
    t.left(30)
    t.forward(25)

t.goto(0, 0)