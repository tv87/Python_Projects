'''
Part A
Define a function drawSquare() that takes two parameters.
(1)Turtle Object
(2)Length of the square

Part B
Use the function in part A to draw five squares of increasing size starting at the same starting point
initialSize = 50
keep adding 25 in the next ones.
'''

# Part A
def draw_Square(size, p):
    size = 100
    for i in range(4):
        p.forward(size)
        p.right(360 / 4)

# Part B      
import turtle
p = turtle.Turtle()
size = 50

for i in range(5):
    draw_Square(size, p)
    side = side + 25

turtle.exitonclick()
