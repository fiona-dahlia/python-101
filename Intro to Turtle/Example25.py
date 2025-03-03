import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("red")
win.title("Example 25")

t1 = turtle.Turtle()
t1.speed("slowest")
t1.color("blue")
t1.pensize(3)

t1.circle(25)
t1.forward(100)
t1.clear()
t1.circle(25)