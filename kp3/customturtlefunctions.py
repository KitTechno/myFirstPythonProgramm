# Autor:              Elia Ressl
# Place:              Homeoffice
# Date:               07.02.2025
# Filename:           customturtlefunctions.py
# Short description:  various functions to make a tictactoe with the turtle lib

#import turtle lib
import turtle

#initialise the windwo for the turtle to move in 
def createwin():
    window = turtle.Screen()
    window.title("🐢")
    window.bgcolor(0.1,0.1,0.19)
    return window

#initialise the turtle
def createturtle(turtlespeed):
    turtlename = turtle.Turtle()
    turtlename.showturtle()
    turtlename.pensize(3)
    turtlename.speed(turtlespeed)
    turtlename.color(0.3,1,0.3)
    return turtlename

#function that draws a square with sidelenght and name of turtle
def square(turtlename,sidelength):
    turtlename.pendown()
    turtlename.setheading(0)
    for i in range(4):
        turtlename.forward(sidelength)
        turtlename.left(90)
    turtlename.penup()

#function that creates a x by y square with the square function
def squarebysquare(turtlename,squaresizex,squaresizey,squarelength):
    for x in range(squaresizex):
        for y in range(squaresizey):
            turtlename.goto(x*squarelength,y*squarelength)
            square(turtlename,squarelength)

# function that creates a circle with the origin in the middle
def createO(turtlename,coordinatex,coordinatey,size):
    turtlename.goto(coordinatex,coordinatey-(size/2)+(size/10))
    turtlename.setheading(0)
    turtlename.pendown()
    turtlename.circle((size/2)-(size/10))
    turtlename.penup()

# function that creates a X with the origin in the middle
def createX(turtlename,coordinatex,coordinatey,size):
    turtlename.goto(coordinatex-(size/2)+(size/10),coordinatey-(size/2)+(size/10))
    turtlename.setheading(45)
    turtlename.pendown()
    turtlename.forward(size+(size/10))
    turtlename.penup()
    turtlename.goto(coordinatex-(size/2)+(size/10),coordinatey+(size/2)-(size/10))
    turtlename.setheading(315)
    turtlename.pendown()
    turtlename.forward(size+(size/10))
    turtlename.penup()

# gets the x coordinate of a tictactoe from an index 1-9
def gridcoordinatex(squareindex,tictactoesize):
    if squareindex == 1 or squareindex == 4 or squareindex == 7:
        gridcoordinatex = (1*tictactoesize)-(tictactoesize/2)
    elif squareindex == 2 or squareindex == 5 or squareindex == 8:
        gridcoordinatex = (2*tictactoesize)-(tictactoesize/2)
    elif squareindex == 3 or squareindex == 6 or squareindex == 9:
        gridcoordinatex = (3*tictactoesize)-(tictactoesize/2)
    return gridcoordinatex

# gets the y coordinate of a tictactoe from an index 1-9
def gridcoordinatey(squareindex,tictactoesize):
    if squareindex == 7 or squareindex == 8 or squareindex == 9:
        gridcoordinatey = (1*tictactoesize)-(tictactoesize/2)
    elif squareindex == 4 or squareindex == 5 or squareindex == 6:
        gridcoordinatey = (2*tictactoesize)-(tictactoesize/2)
    elif squareindex == 1 or squareindex == 2 or squareindex == 3:
        gridcoordinatey = (3*tictactoesize)-(tictactoesize/2)
    return gridcoordinatey
