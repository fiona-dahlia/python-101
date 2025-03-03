import turtle

def draw_spiral(x, y, num_sides, color):
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(x,y)
    t.pencolor(color)
    t.pendown()
    for i in range(50):
        t.forward(i)
        t.left(360/num_sides+2.0)

window = turtle.Screen()
window.setup(800, 600)
window.title('Example 44')

draw_spiral(-100,100,4, "red")
draw_spiral(-100,-100,3, "blue")
draw_spiral(100,-100,5, "green")
draw_spiral(100,100,8, "yellow")