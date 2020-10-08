# Write a program to draw 5 equilateral triangles in a row, same size, length entered from the keyboard
# For turtle
import turtle
paper = turtle.Screen()
pen = turtle.Turtle()
pen.width(5)
pen.color("Red")
pen.speed(8)


length = int(input("Enter size: "))
             

# Draw a triangle using nested loops
for j in range(5):
    for i in range(3):
        pen.forward(length)
        pen.right(360 / 3)
    pen.forward(length)

turtle.exitonclick()


