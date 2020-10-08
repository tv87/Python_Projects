
'''
def f(x):
    answer = x ** 2 + 5
    #return answer
    print(answer)
    
print(f(1))

result = f(2)
print(result)
newResult = 5 * result + 10 / f(1)
'''
'''
Wrire a function that ask the user for first name and last name separately, the fucntion returns the initials
'''
'''
def findInitials():
    fName = (input("Enter first name: "))
    lName = (input("Enter last name: "))
    return (fName[0]. + lName[0])

print("Your inititals are: " + findInitials())
'''
'''
Write a function called isOdd() that takes a parameter called number(integer) and returns true if the number is odd and false otherwise.
'''
'''
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False

num = int(input("Give me a number: "))
print(isOdd(num))
'''
'''
Write a function totalAce() that takes on parameter called scoresList, a list of examScores, the function returns the total number of
A's in the list

An A is a score 82 and above
'''
'''
def totalAs(scoresList):
    # Setup a count
    count = 0
    # Go through each scores in the list
    for score in scoresList:
        # Check if the score is an A
        if score >= 82:
            # Add 1 to your count
            count = count + 1
    # At this point, loop ends
    return count

myList = [72,95,89,45,90]
print(totalAs(myList))
'''
'''
Write a function findAs() that takes one parameter scoresList which is a list of scores, the function returns a list of all A's in the original scoresList.
'''
'''
def findAs(scoresList):
    listOfAs = []
    for score in scoresList:
        if score >= 82:
            listOfAs.append(score)
    return listOfAs

myList = [72,95,89,45,90]
print(findAs(myList))
'''
'''
Write a function findInitials that takes one parameter called nameList - a list of student names, the function returns a string containing the initials of all student names
in the list
print(findInitials(["John", "Jessica", "Adam", "Mileen"])
Hint: use accumulater technique
'''
def findInitials(namesList):
    initials = ""
    for names in namesList:
        firstLetter = name[0]
        initials = initials + firstLetter
    return initials

print(findInitials(["John", "Jessica", "Adam", "Mileen"]))



























            
