import turtle

def midline(t, linelength):
    t.down()
    t.forward(linelength / 2)
    t.backward(linelength)
    t.forward(linelength / 2)

def spiral(t, length, multiplier, numlines, angle):
    for i in range(numlines):
        midline(t, length)
        t.left(angle)
        length = length * multiplier

s = turtle.Screen()
t = turtle.Turtle()

t.left(45)

spiral(t, 50, 1.1, 15, 12)

turtle.exitonclick()
