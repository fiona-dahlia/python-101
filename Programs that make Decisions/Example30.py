import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("Example 30")

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

age = window.numinput("Age Input", "Enter your age here: ")

cost = 0.00

if age < 3 or age > 64:
    t.write(f"Your total is {cost}!", align = "center")
elif age > 2 and age < 13:
    cost = 5.00
    t.write(f"Your total is {cost}!", align = "center")
else:
    cost = 7.00
    t.write(f"Your total is {cost}!", align = "center")
