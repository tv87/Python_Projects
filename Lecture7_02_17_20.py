temp = int(input("Enter a temperature: "))

if temp > 86:
    print("It is hot")
    print("Make sure to drink liquids")
elif temp > 75 and temp <= 86:
    print("It is warm")
elif temp > 55 and temp <= 75:
    print("It is cool")
elif temp > 32 and temp <= 55:
    print("It is cold")
    print("Wear a jacket")
else:
    print("It is freezing")
    
print("Goodbye!")

''' 
