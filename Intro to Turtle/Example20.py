import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgpic('grid.gif')
win.title("Example 20")

t1 = turtle.Turtle()
t1.speed("slowest")
t1.color("red")
t1.pensize(5)

t1.penup()
t1.goto(100, 100)
t1.pendown()
t1.goto(-100, 100)
t1.goto(-100, -100)
t1.goto(100, -100)
t1.goto(100, 100)
