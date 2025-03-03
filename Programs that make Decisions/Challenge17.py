import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 17')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

temp = window.numinput("TEMP", "Enter temperature: ")

if temp == None:
    t.write("YOU CANCELLED", align="center")
elif temp <= 32.00:
    t.pencolor("blue")
    t.write("It is FREEZING", align="center")
elif temp > 32.00 and temp < 70.0:
    t.pencolor("blue")
    t.write("It is COLD", align="center")
elif temp >= 70.0 and temp <= 90:
    t.pencolor("red")
    t.write("It is WARM", align="center")
else:
    t.pencolor("red")
    t.write("It is HOT", align="center")