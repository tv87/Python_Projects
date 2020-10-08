def draw_Triangle(length, pen):
    pen.down()
    for i in range(3):
        pen.forward(length)
        pen.right(360 / 3)

import turtle
myPen = turtle.Turtle()

draw_Triangle(100, myPen)
draw_Triangle(200, myPen)        

length = int(input("Enter the size :"))
pColor = input("Enter a color: ")
myPen.color(pColor)
draw_Triangle(length, myPen)

myPen.width(8)
newLength = int(input("Enter the new length: "))

for i in range(5):
    draw_Triangle(newLength, myPen)
    myPen.forward(newLength)

turtle.exitonclick()
