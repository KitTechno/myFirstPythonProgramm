""" written by Tharani Dayadhi Karunathilaka
https://medium.com/analytics-vidhya/helloworld-with-turtle-graphics-in-python-cd34503c8875 """

# Module laden
import turtle

# ein neues Fenster öffnen
win = turtle.Screen()
win.title("Hello World")
win.bgcolor("light blue")

# erzeugt ein curser mit farbe, grösse und geschwindigkeit
turi = turtle.Turtle()  # eine Schildkröte namens "turi" erzeugen
turi.color("black")     #definiert farbe
turi.pensize(4)         #definiert grösse
turi.speed(10)           #definiert geschwindigkeit

#Schreibt ein H an position -320,0
turi.penup()            #hebt den cursor auf sodass keine linie entsteht
turi.goto(-320, 0)      #sagt dem cursor er soll zu position x,y gehen
turi.pendown()          #lässt den cursor runter sodass eine linie entsteht
turi.left(90)           #rotiert den cursor nach links um x grad
turi.forward(70)        #bewegt den cursor um x units in die richtung die er zeigt   
turi.penup()
turi.goto(-320, 35)
turi.down()
turi.right(90)          #rotiert den cursor nach rechts um x grad
turi.forward(50)
turi.penup()
turi.goto(-270, 70)
turi.pendown()
turi.right(90)
turi.forward(70)

# schreibt ein E an position -260,0
turi.penup()
turi.goto(-260, 0)
turi.pendown()
turi.right(180)
turi.forward(70)
turi.right(90)
turi.forward(35)
turi.penup()
turi.goto(-260, 35)
turi.pendown()
turi.forward(35)
turi.penup()
turi.goto(-260, 0)
turi.pendown()
turi.forward(35)

#schreibt ein L an position -210,70
turi.penup()
turi.goto(-210, 70)
turi.pendown()
turi.right(90)
turi.forward(70)
turi.left(90)
turi.forward(35)

#schreibt ein L an position -165,70
turi.penup()
turi.goto(-165, 70)
turi.pendown()
turi.right(90)
turi.forward(70)
turi.left(90)
turi.forward(35)

#bewegt den cursor
turi.penup()
turi.goto(-90, 70)
turi.pendown()

#schreibt ein O an momentaner position
for i in range(25):
    turi.right(15)
    turi.forward(10)

#schreibt ein W an position -10,70
turi.penup()
turi.goto(-10, 70)
turi.pendown()
turi.right(55)
turi.forward(70)
turi.left(150)
turi.forward(70)
turi.right(155)
turi.forward(70)
turi.left(150)
turi.forward(70)

#bewegt den cursor
turi.penup()
turi.goto(70, 55)
turi.pendown()

#schreibt ein O an momentaner position
for i in range(25):
    turi.right(15)
    turi.forward(10)

#schreibt ein R an position 160,70
turi.penup()
turi.goto(160, 70)
turi.pendown()
turi.right(150)
turi.forward(70)
turi.goto(160, 70)
turi.right(200)
for i in range(20):
    turi.right(15)
    turi.forward(6)
turi.left(180)
turi.forward(60)

#schreibt ein L an position 220,70
turi.penup()
turi.goto(220, 70)
turi.pendown()
turi.right(40)
turi.forward(70)
turi.left(90)
turi.forward(35)

#schreibt ein D an position 290,70
turi.penup()
turi.goto(290, 70)
turi.pendown()
turi.right(90)
turi.forward(70)
turi.penup()
turi.goto(270, 70)
turi.pendown()
turi.left(120)

#macht den bogen für das D
for i in range(15):
    turi.right(15)
    turi.forward(10)

#beendet das programm
turtle.done()