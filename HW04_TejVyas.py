# Tej Vyas
# CS 100 2020S Section 006
# HW04, February 20, 2020

#Exercise 1
a,b,c = 3,4,5

if a < b:
    print('OK')

if c < b:
    print('OK')

if a + b == c:
    print('OK')

if a * a + b * b == c * c:
     print('OK')

#Exercise 2
a, b, c = 3, 4, 5

if a < b: 
   print('OK');
else:
   print('NOT OK'); 

if c < b: 
   print('OK');
else:
   print('NOT OK'); 

addition = a + b 

if addition == c: 
   print('OK');
else:
   print('NOT OK'); 


addition = (a * a) + (b * b)

if addition == c: 
   print('OK');
else:
   print('NOT OK');


#Exercise 3
import turtle

My_turtle = turtle.Turtle()
My_turtle.forward(50)   
My_turtle.left(90)
My_turtle.forward(50)
My_turtle.left(90)
My_turtle.forward(50)
My_turtle.left(90)
My_turtle.forward(50)
My_turtle.left(90)

import turtle
My_turtle = turtle.Turtle()
My_turtle.forward(130)

import turtle
def draw_triangle():

    window = turtle.Screen()
    window.bgcolor("yellow") 

    My_turtle = turtle.Turtle()
    My_turtle.forward(100)
    My_turtle.left(120)
    My_turtle.forward(100)
    My_turtle.left(120)
    My_turtle.forward(100)
  
  
draw_triangle()

import turtle
def draw_triangle():
  
    window=turtle.Screen()
    window.bgcolor("black") 
  
    My_turtle = turtle.Turtle()
    My_turtle.color("blue")
    My_turtle.pensize(20)
    My_turtle.forward(100)
    My_turtle.left(120)
    My_turtle.forward(100)
    My_turtle.left(120)
    My_turtle.forward(100)
  
  

    window.exitonclick()

draw_triangle()
  
