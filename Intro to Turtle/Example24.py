import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title("Example 24")

t1 = turtle.Turtle()
t1.speed("slowest")
t1.color("orange")
t1.pensize(3)

t1.fillcolor("cyan")
t1.begin_fill()

t1.goto(-120, 66)
t1.goto(88, 55)
t1.goto(43, -99)
t1.goto(-33, -55)
t1.home()
t1.end_fill()