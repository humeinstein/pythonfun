from turtle import *
from random import randint

#turtle speed 
speed(4)

#*******************GAME MAP*********************
#write() writes text to screen
#penup lift pen to not mark
#right(90) means rotate 90degrees to right
penup()
goto(-140, 140)
#0---1---2---3---4---5
for step in range(11):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(25)

#**************END OF GAME MAP *********************
#***********Init turtles and position**************
andrew = Turtle()
andrew.color('red')
andrew.shape('turtle')
andrew.penup()
andrew.goto(-160, 100)
andrew.pendown()

kelly = Turtle()
kelly.color('blue')
kelly.shape('turtle')
kelly.penup()
kelly.goto(-160, 70)
kelly.pendown()

for turn in range(100):
    andrew.forward(randint(1,5))
    kelly.forward(randint(1,5))
