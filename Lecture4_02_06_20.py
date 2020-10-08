import turtle
paper = turtle.Screen()
pen = turtle.Turtle()
pen.color("Red")
pen.width(7.5)
pen.speed(8)

sidelength = 100
gap = 15

for i in range(4):
    pen.forward(sidelength)
    pen.right(90)


pen.up()
pen.forward(sidelength + gap)
pen.down()

for i in range(4):
    pen.forward(sidelength)
    pen.right(90)

pen.up()
pen.forward(sidelength + gap)
pen.down()
pen.setheading(45)

for i in range(4):
    pen.forward(sidelength)
    pen.right(90)
    
paper.exitonclick()
