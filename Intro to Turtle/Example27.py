import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title("Example 27")

t = turtle.Turtle()
t.penup()

yourName = win.textinput("Name input", "Enter your name: ")
t.goto(-50, 100)
t.write(f"{yourName}", align="center")

yourAge = win.textinput("Age input", "Enter your age: ")
t.goto(-50, 100)
t.write(f"{yourAge}", align="center")