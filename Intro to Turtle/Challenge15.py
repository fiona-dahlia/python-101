import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title('Challenge 15 - Draw Your Name')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("red")
t.penup()

t.goto(-50, 100)
t.write("Fiona Kamaraj", align="center", font=("Arial", "24", "bold"))