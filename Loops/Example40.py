import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("Example 40")

t = turtle.Turtle()
t.speed("fastest")

colors = ("red", "blue")

for x in range(-400, 400, 75):
    row = 1
    for y in range(300, -300, -75):
        t.penup()
        t.goto(x, y)
        t.pendown()

        if row % 2 == 0:
            t.fillcolor("red")
        else:
            t.fillcolor("blue")

        t.begin_fill()
        t.circle(25)
        t.end_fill()
        row = row + 1