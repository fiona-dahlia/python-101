import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title("Example 23")

t1 = turtle.Turtle()
t1.speed("slow")
t1.color("orange")
t1.pensize(3)

t1.penup()
t1.forward(100)
t1.pendown()

t1.fillcolor("blue")
t1.begin_fill()

t1.forward(100)
t1.left(360/3)
t1.forward(100)
t1.left(360/3)
t1.forward(100)
t1.left(360/3)
t1.end_fill()

t1.hideturtle()