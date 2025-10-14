import turtle

turtle.penup()
turtle.hideturtle()

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELT_X = -40
LEFT_BELT_Y = -20

MID_BELT_X = 0
MID_BELT_Y = 0

RIGHT_BELT_X = 40
RIGHT_BELT_Y = 20

LEFT_LEG_X = -90
LEFT_LEG_Y = -180

RIGHT_LEG_X = 120
RIGHT_LEG_Y = -140

turtle.goto(LEFT_SHOULDER_X ,LEFT_SHOULDER_Y)
turtle.dot()
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.dot()
turtle.write('Meissa')
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.dot()
turtle.write('Alnitak')
turtle.goto(MID_BELT_X, MID_BELT_Y)
turtle.dot()
turtle.write('Alnilam')
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)
turtle.dot()
turtle.write('Mintaka')
turtle.goto(LEFT_LEG_X, LEFT_LEG_Y)
turtle.dot()
turtle.write('Saiph')
turtle.goto(RIGHT_LEG_X, RIGHT_LEG_Y)
turtle.dot()
turtle.write('Rigel')

turtle.goto(LEFT_SHOULDER_X ,LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.goto(MID_BELT_X, MID_BELT_Y)
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)
turtle.goto(RIGHT_SHOULDER_X,RIGHT_SHOULDER_Y)
turtle.penup()
turtle.goto(LEFT_LEG_X, LEFT_LEG_Y)
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y)
turtle.penup()
turtle.goto(RIGHT_LEG_X, RIGHT_LEG_Y)
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y)

turtle.done()