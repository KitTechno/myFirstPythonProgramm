# Autor:              Elia Ressl
# Place:              Homeoffice
# Date:               08.02.2025
# Filename:           tictactoe.py
# Short description:  

#imports the custom functions required for the tic tac toe
import customturtlefunctions as turtlefunc

#creates a windwo with my custom specifications
window = turtlefunc.createwin()
#creates a turtle with my custom specifications
gapa = turtlefunc.createturtle(10)

tictactoesize = 50
turtlefunc.squarebysquare(gapa,3,3,tictactoesize)

# asks 9 times for user input 1 or 2. 1 is always a circle and 2 is always a square
for i in range(9):
    if i % 2 == 0:
        squareindex = int(input("player 1 enter 1-9: "))
        coordinatex = turtlefunc.gridcoordinatex(squareindex,tictactoesize)
        coordinatey = turtlefunc.gridcoordinatey(squareindex,tictactoesize)
        turtlefunc.createO(gapa,coordinatex,coordinatey,tictactoesize)
    else:
        squareindex = int(input("player 2 enter 1-9: "))
        coordinatex = turtlefunc.gridcoordinatex(squareindex,tictactoesize)
        coordinatey = turtlefunc.gridcoordinatey(squareindex,tictactoesize)
        turtlefunc.createX(gapa,coordinatex,coordinatey,tictactoesize)

window.mainloop()
