import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 17')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

temp = window.numinput("Temperature", "Enter temperature outside: ")
wind_speed = window.numinput("Wind Speed", "Enter wind speed: ")

if temp == None:
    t.write("YOU CANCELLED", align="center")
elif temp <= 32.00:
    t.pencolor("blue")
    t.write("It is FREEZING", align="center")

    if wind_speed > 20.0 and wind_speed < 40.00:
        t.goto(0, -100)
        t.write("Moderate Risk of frost bite.", align="center")
    elif wind_speed > 40.00:
        t.goto(0, -100)
        t.write("Severe Risk of frost bite.", align="center")

elif temp > 32.00 and temp < 70.00:
    t.pencolor("blue")
    t.write("It is COLD", align="center")
elif temp >= 70.00 and temp <= 90.00:
    t.pencolor("red")
    t.write("It is WARM", align="center")
else:
    t.pencolor("red")
    t.write("It is HOT", align="center")

    # add these lines for solution
    if wind_speed > 25.0 and wind_speed < 35.00:
        t.goto(0, -100)
        t.write("Moderate Risk of wind burn.", align="center")
    elif wind_speed >= 35.00:
        t.goto(0, -100)
        t.write("Severe Risk of wind burn.", align="center")