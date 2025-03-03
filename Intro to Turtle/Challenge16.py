import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title('Challenge 16')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("blue")
t.penup()

yourName = win.textinput("Name Input", "Enter your name:")

x = win.numinput("X Input", "Enter x coordinate:", 0, minval=-400, maxval=400)

y = win.numinput("Y Input", "Enter y coordinate:", 0, minval=-300, maxval=300)

t.goto(x, y)
t.write(f"{yourName}")