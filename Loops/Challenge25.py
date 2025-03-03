import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 25')

t = turtle.Turtle()
t.speed("slowest")

colors = ("red", "blue", "green", "yellow", "black")

i = 0
while i < len(colors):
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    i = i + 1
