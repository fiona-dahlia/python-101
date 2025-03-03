import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title("Example 26")

t = turtle.Turtle()
t.speed("slow")
t.pencolor("blue")
t.penup()

t.goto(-150, 100)
t.write("Hello World!")

t.goto(-150, 50)
t.write("Hello World Bigger!", font=("Arial", "24", "normal"))

t.goto(-150, 0)
t.write("Hello World Bold!", font=("Arial", "24", "bold"))
