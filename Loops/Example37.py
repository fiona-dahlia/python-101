import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("Example 37")

t = turtle.Turtle()
t.speed("fast")
t.pensize(2)
t.pencolor("yellow")

for x in range(360):
    t.forward(2 * x)
    t.left(144)