#adds turle lib
import turtle

#initialise the windwo for the turtle to move in 
win = turtle.Screen()
win.title("🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢🐢")
win.bgcolor(0.1,0.1,0.19)

#initialise the turtle turi
turi = turtle.Turtle()
turi.showturtle()
turi.pensize(5)
turi.speed(10)
turi.color(0.3,1,0.3)

startingx = -500
startingy = 0

#go to position x,y
turi.penup()
turi.goto(startingx+0,startingy)
#draw an H at current position starting at the bottom left
turi.pendown()
turi.setheading(90)
turi.forward(100)
turi.backward(50)
turi.setheading(0)
turi.forward(50)
turi.setheading(90)
turi.forward(50)
turi.backward(100)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+100,startingy)
#draw an E at current position starting at the bottom left
turi.pendown()
turi.setheading(0)
turi.forward(50)
turi.backward(50)
turi.setheading(90)
turi.forward(50)
turi.setheading(0)
turi.forward(50)
turi.backward(50)
turi.setheading(90)
turi.forward(50)
turi.setheading(0)
turi.forward(50)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+200,startingy)
#draw an L at current position starting at the bottom left
turi.pendown()
turi.setheading(0)
turi.forward(50)
turi.backward(50)
turi.setheading(90)
turi.forward(100)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+300,startingy)
#draw an L at current position starting at the bottom left
turi.pendown()
turi.setheading(0)
turi.forward(50)
turi.backward(50)
turi.setheading(90)
turi.forward(100)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+400,startingy)
#draw a circle
turi.setheading(0)
turi.forward(50)
turi.setheading(90)
turi.forward(50)
turi.pendown()
turi.begin_fill()
turi.circle(50)
turi.color(0.3,0.3,1)
turi.end_fill()
turi.color(0.3,1,0.3)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+500,startingy)
#draw an V at current position starting at the bottom left
turi.penup()
turi.setheading(90)
turi.forward(100)
turi.pendown()
turi.setheading(270+(90/4))
turi.forward(110)
turi.setheading(45+(90/4))
turi.forward(110)

#go to position x,y
turi.penup()
turi.goto(startingx+550,startingy)
#draw an V at current position starting at the bottom left
turi.penup()
turi.setheading(90)
turi.forward(100)
turi.pendown()
turi.setheading(270+(90/4))
turi.forward(110)
turi.setheading(45+(90/4))
turi.forward(110)

#go to position x,y
turi.penup()
turi.goto(startingx+700,startingy)
#draw a circle¨
turi.setheading(0)
turi.forward(50)
turi.setheading(90)
turi.forward(50)
turi.pendown()
turi.begin_fill()
turi.circle(50)
turi.color(0.3,0.3,1)
turi.end_fill()
turi.color(0.3,1,0.3)
turi.penup()
# turi.color(0.3,0,3,1)

#go to position x,y
turi.penup()
turi.goto(startingx+800,startingy)
#draw an R at current position starting at the bottom left
turi.pendown()
turi.setheading(90)
turi.forward(100)
turi.setheading(0)
turi.begin_fill()
x=0
while(x<18):
    x=x+1
    turi.forward(5)
    turi.right(10)
turi.color(0.3,0.3,1)
turi.end_fill()
turi.color(0.3,1,0.3)
turi.goto(startingx+800,startingy+50)
turi.setheading(270+37)
turi.forward(65)

#go to position x,y
turi.penup()
turi.goto(startingx+900,startingy)
#draw an L at current position starting at the bottom left
turi.pendown()
turi.setheading(0)
turi.forward(50)
turi.backward(50)
turi.setheading(90)
turi.forward(100)
turi.penup()

#go to position x,y
turi.penup()
turi.goto(startingx+1000,startingy)
#draw an D at current position starting at the bottom left
turi.pendown()
turi.setheading(90)
turi.forward(100)
turi.setheading(0)
turi.begin_fill()
x=0
while(x<15):
    x=x+1
    turi.forward(11)
    turi.right(12.5)
turi.color(0.3,0.3,1)
turi.end_fill()
turi.color(0.3,1,0.3)

while(1):
    turi.setheading(0)
    turi.pensize(10)
    turi.pencolor(1,0.3,0.3)
    turi.penup()
    turi.goto(-550,-50)
    turi.pendown()
    turi.goto(600,-50)
    turi.goto(600,150)
    turi.goto(-550,150)
    turi.goto(-550,-50)

turtle.done