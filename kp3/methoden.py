# Autor:              Elia Ressl
# Place:              Homeoffice
# Date:               07.02.2025
# Filename:           methoden.py
# Short description:  Erste übung mit Methoden. es hat zwei methoden die benutzt werden um ein quadrat mit x und y quadraten und x seitenlänge zu zeichnen

#import turtle lib
import turtle

#function that draws a square with sidelenght and name of turtle
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
    turtlename.penup()

#function that creates a x by y square with the square function
def squarebysquare(squaresizex,squaresizey,squarelength,turtlename):
    for x in range(squaresizex):
        for y in range(squaresizey):
            turtlename.goto(x*squarelength,y*squarelength)
            square(turtlename,squarelength)


#initialise the windwo for the turtle to move in 
window = turtle.Screen()
window.title("🐢")
window.bgcolor(0.1,0.1,0.19)

#initialise the turtle gapa (galapagos)
gapa = turtle.Turtle()
gapa.showturtle()
gapa.pensize(3)
gapa.speed(10)
gapa.color(0.3,1,0.3)

#variables to change the output of following squarebysquarefunction
turtlename=gapa
squarelength=5
squaresizex=10
squaresizey=10

#calls the function to draw the x by y square
squarebysquare(squaresizex,squaresizey,squarelength,turtlename)

# x=0
# while(x<3):
#     y=0
#     while(y<3):
        # gapa.goto(x*squarelength,y*squarelength)
        # square(gapa,squarelength)
#         y=y+1
#     x=x+1
#hab erst später realisiert das for x in range(3)auch funktionieren würde und einfacher wäre

turtle.done()
