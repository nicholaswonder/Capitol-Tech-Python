import turtle
turtle.setup(600,600)

#Octagon code
for count in range(8):
    turtle.forward(100)
    turtle.right(45)

turtle.textinput("Pause", "Press Enter To Continue...")

#Circle Code
turtle.clear()
turtle.speed(0)
radius = 20
offset = 10
num_circles = turtle.numinput("Circles","How many circles? (1-30)", 15, 1, 30)

for count in range(int(num_circles)):
    turtle.circle(radius)

    x = turtle.xcor()
    y = turtle.ycor() - offset

    radius += offset

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.textinput("Pause", "Press Enter To Continue...")

turtle.goto(0,0)
turtle.clear()

num_circles = turtle.numinput("Circles","How many circles? (1-60)", 30,1,60)
angle = 360.0 / float(num_circles)

for count in range(int(num_circles)):
    turtle.circle(75)
    turtle.left(angle)

turtle.textinput("Pause", "Press Enter To End Program...")