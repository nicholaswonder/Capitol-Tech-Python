import turtle

def window(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(25)
        turtle.left(90)
    turtle.end_fill()

def building(height):
    turtle.fillcolor('gray')
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    turtle.right(90)
    turtle.penup()

def stars():
    print()

def buildings():

    turtle.penup()
    turtle.goto(-600,-600)
    turtle.setheading(90)
    building(700)
    turtle.goto(-600, -400)
    building(500)
    turtle.goto(-600, -400)
    building(1000)
    turtle.goto(-600, -200)
    building(400)
    turtle.goto(-600, 0)
    building(300)
    turtle.goto(-600, 200)
    building(800)
    turtle.goto(-600, 400)

turtle.speed(0)
buildings()
input()