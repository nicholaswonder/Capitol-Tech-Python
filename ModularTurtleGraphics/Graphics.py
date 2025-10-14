import turtle

# draw squares
def square(x,y,width,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

# Draw Circles
def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Draw Lines
def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX,startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX,endY)

if __name__ == '__main__':
    print("1. Draw Squares")
    print("2. Draw Circles")
    print("3. Draw Lines")

    option = int(input("Select a program to execute: "))
    turtle.hideturtle()

    if option == 1:
        square(100, 0, 50, 'red')
        square(-150, -100, 200, 'blue')
        square(-200, 150, 75, 'green')
    elif option == 2:
        circle(0, 0, 100, 'red')
        circle(-150, -75, 50, 'blue')
        circle(-200, 150, 75, 'green')
    elif option == 3:
        line(0, 100, -100, -100, 'red')
        line(0, 100, 100, -100, 'blue')
        line(-100, -100, 100, -100, 'green')
    input()