'''
def windmill(t, side, num, angle):
    t.pendown()
    for j in range(num):
        t.forward(3 * side)
        for i in range(4):
            t.forward(side)
            t.right(90)
        t.backward(3 * side)
        t.right(angle)
   
import turtle
speedy = turtle.Turtle()
windmill(speedy, 35, 12, 30)

turtle.exitonclick()
'''
'''
def isAnagram(listA, listB):
    listA.sort()
    listB.sort()
    return listA == listB
'''
'''
    if len(listA) != len(listB):
        return False
    for element in listA:
        if listA.count(element) != listB.count(element):
            return False
    return True    

print(isAnagram([14, 10, 19], [10, 14, 19]))
'''
'''
def extractEvenLess(intList):
    threshold = (int("Enter the threshold value: "))
    myList = []
    for elements in intList:
        if elements % 2 == 0 and number < value:
            myList.append()
            return myList
                        
lst = [9, 24, 95, 198, 205, 1, 48, 23, 165, 240]
result = extractEvenLess(lst)
print(result)
'''
'''
def month_info(medium_Length):
    month = input("What month is it? ")
    numDays = int(input("Howmany days in the month: " + month + "? "))
    if numDays > medium_Length:
        print(month, "is long")
    elif numDays == medium_Length:
        print(month, "is medium")
    else:
        print(month, "is short")
    return month

current_month = month_info(30)
print(current_month)
'''
'''
def stair(t, thread_size, riser_height):
    t.pendown()
    t.forward(thread_size)
    t.right(90)
    t.forward(riser_height)
    t.left(90)

def staircase(t, num_stairs, thread_size, riser_height):
    for i in range(num_stairs):
        stair(t, thread_size, riser_height)

import turtle
s = turtle.Screen()
aTurt = turtle.Turtle()
staircase(aTurt, 3, 100, 50)


turtle.exitonclick()
'''
'''
chain = [1, '2', 3, '4']
leading = chain[:1]
trailing = chain[-1:]
print(leading + trailing)
'''
'''
import turtle
s = turtle.Screen()
t = turtle.Turtle()
for i in range(7):
    if i%4 == 0:
        t.forward(50)
        t.right(90)
'''
def sliceAndDice(name):
    mystery = []
    recycle = []
    for item in name:
        if item in mystery:
            recycle.append(item)
        else:
            mystery.append(item)
    return len(mystery)
print(sliceAndDice(['t', 'e', 'nn', 'e', 'ss', 'ee']))

            


















