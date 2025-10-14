import turtle

TARGET_X = 100
TARGET_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(600,600)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_X, TARGET_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(SPEED)

angle = float(input("Enter the projectile angle: "))
force = float(input("Enter the launch force (1-10): "))

distance = force * FORCE_FACTOR

turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)

if  TARGET_X <= turtle.xcor() <= (TARGET_X + TARGET_WIDTH) and TARGET_Y <= turtle.ycor() <= (TARGET_Y + TARGET_WIDTH):
    print("Target Hit!")
else:
    print("You Missed...")