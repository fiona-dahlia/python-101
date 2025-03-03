import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 26')

t = turtle.Turtle()
t.speed("fastest")

colors = ("green", "blue")

for y in range(300, -300, -75):
    column = 1
    for x in range(-400, 400, 75):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(colors[column % len(colors)])
        t.begin_fill()

        for i in range(0, 4):
            t.forward(50)
            t.left(90)

        t.end_fill()
        column = column + 1
