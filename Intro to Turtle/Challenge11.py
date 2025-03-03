import turtle

win = turtle.Screen()
win.setup(800, 600)
win.bgpic('grid.gif')
win.title("Challenge 11")

t1 = turtle.Turtle()
t1.speed("slowest")
t1.color("green")
t1.pensize(5)

t1.penup()
t1.goto(150, 150)
t1.pendown()
t1.goto(-150, 150)
t1.goto(-150, -50)
t1.goto(150, -50)
t1.goto(150, 150)