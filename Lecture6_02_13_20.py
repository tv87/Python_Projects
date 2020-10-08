'''
Part A: Write a function draw_Flag that draws an equilateral triangle of a specified size. The function takes two parameters.
(1) t: a turtle object
(2) side: the side length of the flag
'''

import turtle
pen = turtle.Turtle()

def draw_Flag(t, side):
    t.down()
    for i in range(3):
        t.forward(side)
        t.right(360/3)

'''
Part B: Define a function flag_Line() that uses the function draw_Flag() to draw a line of flag that is a line of consequetive flags.
The function takes 3 parameters.
(1)t: a turtle object
(2) length: side length
(3) numOfFlags: number of flags in the line
'''

sideLength = 100


def flag_Line(t, length, numOfFlags):
    for i in range(numOfFlags):
        draw_Flag(t, length)
        t.forward(length)


'''
Part C: Use the flag_Line function to deaw 2 flag lines with the same starting point:
(1) vertical flagline of 2 triangles of size 150
(2) tilted at 45 degrees angle flagline 4 triangles of size 45
'''

pen.setheading(90)
flag_Line(pen, 150, 2)
pen.backward(300)
pen.setheading(45)
flag_Line(pen, 45, 4)



'''
Part D: Use the flag_Line() in part C to draw a square of flaglines of 3 flags each and size 40
Hint: For full credit you must use loops
'''
pen.setheading(0)
for i in range(4):
    flag_Line(pen, 40, 3)
    pen.left(90)

turtle.exitonclick()



