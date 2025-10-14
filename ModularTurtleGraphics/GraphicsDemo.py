import turtle
import Graphics

x1 = 0
y1 = 100
x2 = -100
y2 = -100
x3 = 100
y3 = -100
radius = 50

def main():
    turtle.hideturtle()

    Graphics.square(x2,y2,(x3-x2),'gray')

    Graphics.circle(x1,y1,radius,'blue')
    Graphics.circle(x2,y2,radius,'red')
    Graphics.circle(x3,y3,radius,'green')

    Graphics.line(x1,y1,x2,y2,'black')
    Graphics.line(x1,y1,x3,y3,'black')
    Graphics.line(x2,y2,x3,y3,'black')

if __name__ == '__main__':
    main()