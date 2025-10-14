import turtle
from tkinter.constants import CENTER

turtle.setup(600,600)
turtle.speed(0)

#Repeating Squares
length = 0
turtle.setheading(90)
for count in range(50):
    length += 5
    for count2 in range(4):
        turtle.forward(length)
        turtle.left(90)

turtle.textinput("Pause", "Press Enter To Continue...")

turtle.setheading(0)
turtle.goto(0,0)
turtle.clear()

#Star Pattern
turtle.right(45)
for count in range(8):
    turtle.forward(200)
    turtle.right(135)

turtle.textinput("Pause", "Press Enter To Continue...")

turtle.setheading(0)
turtle.goto(0,0)
turtle.clear()

#Hypnotic Pattern
length = 5
for count in range(49):
    turtle.left(90)
    turtle.forward(length)
    length += 5

turtle.textinput("Pause", "Press Enter To Continue...")

turtle.setheading(0)
turtle.goto(0,0)
turtle.clear()

#Stop Sign
turtle.write("STOP", False, CENTER)
turtle.setheading(90)
turtle.penup()
turtle.forward(70)
turtle.left(90)
turtle.forward(25)
turtle.setheading(0)
turtle.pendown()

for count in range(8):
    turtle.forward(50)
    turtle.right(45)

turtle.textinput("Pause", "Press Enter To End Program...")