import turtle


def square(turtlename,sidelength):
    turtlename.pendown()
    turtlename.setheading(0)
    turtlename.forward(sidelength)
    turtlename.right(90)
    turtlename.forward(sidelength)
    turtlename.right(90)
    turtlename.forward(sidelength)
    turtlename.right(90)
    turtlename.forward(sidelength)

#initialise the windwo for the turtle to move in 
window = turtle.Screen()
window.title("🐢")
window.bgcolor(0.1,0.1,0.19)

#initialise the turtle turi
gapa = turtle.Turtle()
gapa.showturtle()
gapa.pensize(5)
gapa.speed(4)
gapa.color(0.3,1,0.3)

squarelength=122

x=0
while(x<3):
    y=0
    while(y<3):
        gapa.penup()
        gapa.goto(x*squarelength,y*squarelength)
        gapa.pendown()
        square(gapa,squarelength)
        gapa.penup()
        y=y+1
    x=x+1


turtle.done()

