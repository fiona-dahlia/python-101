import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgpic('grid.gif')
win.title("Example 22")

t1 = turtle.Turtle()
t1.speed("fast")
t1.color("orange")
t1.pensize(3)

t1.circle(100)
t1.left(90)
t1.circle(100)
t1.left(90)
t1.circle(100)
t1.left(90)
t1.circle(100)