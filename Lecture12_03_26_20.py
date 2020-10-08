'''
Write a program that returns the number of repeated words
'''
'''
def repeatedWords(paragraph):
    repeated = []
    wordsList = paragraph.split()

    index = 0
    while index < len(wordsList):
        word = wordsList[index]
        if wordsList.count(word) > 1 and word not in repeated:
            repeated.append(word)

        index += 1

    return len(repeated)

text = ''''''it is what it is
exam is online
exam is accumulative''''''
print(repeatedWords(text))
'''
'''
Define a function numDigits() that takes an integer parameter, number and returns its number
of digits, For examplr, if number = 2343, the function returns 4.
'''
'''
# print(repeatedWords(text))

def numDigits(number):
    total = 0

    while number > 0:
        number = number //10 # number becomes smaller
        total += 1 # total increased by one

    return total

print(numDigits(2343782))
'''
'''
Python random module contains a function randint(a,b) that geneates a random integer between
a and b, inclusive. Write a function rollDie() that uses the randint function,
eg. math.randint(1, 6), to simulate rolling of a die and repeatedly
'''
'''
# while die < 6, keep rolling and increment your count
def rollDie1():
    count = 0
    die = random.randint(1, 6)

    while die < 6:
        print(die)
        count += 1
        die = random.randint(1, 6)
    return count

import random
print("number of tries to get 6: ", rollDie1())

def rollDie2():
    count = 0

    while True:
        print(die)
        die = random.randint(1, 6)
        if die == 6:
            break
        count += 1

    return count

import random
print("number of tries to get 6: ", rollDie2())
'''
'''
Write a function firstLongWordInLine() that takes two parameters:
- text,
- length
the function returns a list containing, for each line in text,the first word that has more
than 'length' characters or empty string if no such a word exist in the line.
'''
def firstLongWordInLine(text, length):
    answer = []
    listOfLines = text.split('\n')

    for line in listOfLines: # goes through each line
        wordsList = line.split()# get the words in line
        wordsToAdd = ''
        for word in wordsList:
            if len(word) > length:
                wordsToAdd = word
                break
        answer.append(wordsToAdd)
    return answer

text = '''Today you are you
that is truer than true
There is no one alive
who is more than you'''
print(firstLongWordInLine(text, 4))

            












































