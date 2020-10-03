# Tej Vyas
# CS 100 2020S Section 006
# HW 12, April 30, 2020

# Problem 1
def safeOpen(filename):
    try:
        f = open(filename)
        return f
    except FileNotFoundError:
        return None
print(safeOpen("ghost.txt"))

# Problem 2
def safeFloat(x):
    try:
        return float(x)
    except:
        return 0.0
f = safeFloat('abc')
print(f)
f = safeFloat(6.7)
print(f)

# Problem 3
def averageSpeed():
    count = 0
    file = None
    while count != 2:
        filename = input("Enter file name: ")
        file = safeOpen(filename)
        if file:
            break
        count = count + 1
        if count <= 1:
            print("Please try again.")
        if count == 2:
            print(" Yet another human error. Goodbye....")
            exit(0)


    sum =0
    counter =0
    for line in file.read().split():
        num = safeFloat(line)
        if num >= 2:
             sum += num
             counter += 1
    file.close()
    avg = sum /counter
    print("Average speed is {0:.2f}".format(avg), " miles per hour.")


if __name__ == "__main__":
   averageSpeed()

                
    
