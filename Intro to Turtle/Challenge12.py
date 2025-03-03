import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgpic('grid.gif')
win.title("Challenge 12")

t1 = turtle.Turtle()
t1.speed("slow")
t1.color("red")
t1.pensize(5)

t1.penup()
t1.goto(120, -90)
t1.pendown()

t1.forward(100)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(100)
t1.right(90)
t1.forward(100)