import turtle
def draw_star(x, y, color):
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x, y)
    t.pensize(10)
    t.pencolor(color)
    t.pendown()
    for i in range(80):
        t.forward(i)
        t.left(144)

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 29')

draw_star(-100, 100, "red")  # top left corner
draw_star(-100, -100, "blue")  # bottom left corner
draw_star(100, -100, "green")  # bottom right corner
draw_star(100, 100, "yellow")  # top right corner
draw_star(0, 0, "orange")