# Tej Vyas
# CS 100 2020S Section 006
# HW 08, March 25, 2020

# Problem 1

def twoWords(l,f):

    word1 = ""

    word2= ""

    while True:

        word1 = input('\nA ' + str(l) + '-letter word please.: ')

        if l == len(word1):

            break

    while True:
        
        word2 = input('\nA word beginning with ' + f+ ' please.: ')

        if word2[0] == f.upper() or word2[0] == f.lower():

            break

    return [word1,word2]

length=int(input('Enter length: '))

letter=input('\nEnter a letter: ')

print(twoWords(length,letter))


# Problem 2

def twoWords(l,f):


    word1 = ""
    word2= ""

    word1 = input('\nA ' + str(l) + '-letter word please.: ')

    while ( l != len(word1)):

        word1 = input('\nA ' + str(l) + '-letter word please.: ')

        word2 = input('\nA word beginning with ' + f+ ' please.: ')
  
    while ((word2[0]!= f.upper()) & (word2[0]!= f.lower())):
  
         word2 = input('\nA word beginning with ' + f+ ' please.: ')

    return [word1,word2]

length=int(input('Enter length: '))
letter=input('\nEnter a letter: ')

print(twoWords(length,letter))


# Problem 3

def password():

    while True:

        s = input("\n\nEnter password: ")

        if 15 < len(s) < 8 or sum(str.isdigit(c) for c in s) < 1:

            print("Password must be 8-15 chars long and contain at least one digit:")

            continue

        else:

            print("The password is valid.")

            break

password()

# Problem 4

import random

def GuessNumber():
    print("I'm thinking of a number in the range 0-5-. You have five tries to guess it.")

    number=random.randint(1,50)

    countValue=1

    print("Guess",countValue,end='')
    userToguess=int(input("?"))

    while number!=userToguess:
        if(countValue==5 or userToguess==number):

            print("Sorry you have used all tries! The correct number is ", number)
            break;
        if userTOguess<number:
            print(userToguess,"is too low")
            countValue=countValue+1
            print("Guess", countValue,end="")

            userToguess = int(input("? "))

        elif userToguess > number:

            print(userToguess,"is too high")

            countValue = countValue + 1

            print("Guess", countValue,end ="")

            userToguess = int(input("? "))

        else:

            print ("you are right! I was thinking of ", userToguess,"!")

            break



GuessNumber()

  



