import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgpic('grid.gif')
win.title("Example 21")

t1 = turtle.Turtle()
t1.speed("slow")
t1.color("purple")
t1.pensize(6)

t1.right(360/4)
t1.forward(200)
t1.right(360/4)
t1.forward(200)
t1.right(360/4)
t1.forward(200)
t1.right(360/4)
t1.forward(200)