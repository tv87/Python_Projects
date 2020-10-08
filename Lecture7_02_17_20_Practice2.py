'''
Write a program that ask the user for a line of text, the program print to the screen
            every vowel that appear in the message in the same order as they  appear

Example
userInput = "Hello"
output - >
e
o
'''
message = (input("Enter message: "))
vowel = "aeiou"
for char in message:
    if char in vowel:
        print(char)

        
