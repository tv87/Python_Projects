# Tej Vyas
#CS 100 2020S Section 006
#HW03, February 6, 2020

# Question 1
import turtle
paper = turtle.Screen()
p = turtle.Turtle()
sidelength = 100
p.color("Purple")
p.width(4)
p.speed(8)

def eqTriangle():
    p.right(60)
    for i in range(3):
        p.forward(sidelength)
        p.right(120)

def square():
    p.left(60)
    for i in range(4):
        p.forward(sidelength)
        p.right(90)

def pentagon():
    for i in range(5):
        p.forward(sidelength)
        p.right(72)
        
        
p.penup()
p.goto(-100,0)
p.pendown()
eqTriangle()

p.penup()
p.goto(0,0)
p.pendown()
square()

p.penup()
p.goto(170,0)
p.pendown()
pentagon()
p.clear()


# Question 2
p.penup()
p.home()

for i in [50, 100, 150, 200]:
    p.right(90)
    p.forward(i)
    p.right(270)
    p.pendown()
    p.circle(i)
    p.penup()
    p.home()

paper.exitonclick()

# Question 3
import math

ans = math.factorial(100)
print('Question #3A\nFactorial of 100 is: ', ans)
ans = math.log(1000000, 2)
print('Question #3B\nLog of 1,000,000 base 2 is: ', ans)
ans = math.gcd(63, 49)
print('Question #3C\nGCD of 63 and 49 is: ', ans) 
