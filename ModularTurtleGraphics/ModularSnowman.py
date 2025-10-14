import turtle

def DrawBase():
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    turtle.circle(100)

def DrawMid():
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(50)

def DrawArms():
    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.goto(100,0)
    turtle.penup()
    turtle.goto(-50,-50)
    turtle.pendown()
    turtle.goto(-100,0)

def DrawHead():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(10,30)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(-10, 30)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(-10,10)
    turtle.pendown()
    turtle.goto(10,10)

def DrawHat():
    turtle.penup()
    turtle.goto(-40,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(40,50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()

def main():
    turtle.hideturtle()
    DrawBase()
    DrawMid()
    DrawArms()
    DrawHead()
    DrawHat()
    input("Press Enter to End")

if __name__ == '__main__':
    main()