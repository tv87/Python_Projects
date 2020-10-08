'''
Write a program that asks the user for his/her age.
The program prints whether the person is eligible to vote as well as his/her drink or drive
'''

age = int(input("Enter your age: "))

if age >= 21:
    print("You can drink. You can drive. You can vote")
elif age >= 18:
    print("You can not drink. You can drive. You can vote.")
elif age >=16:
    print("You can not drink. You can drive. You can not vote.")
else:
    print("You can not drink. You can not drive. You can not vote.")
    
