outFile = open("output.txt", 'w')

# write(1 string)
for i in range(5):
    outFile.write("hello " + str(i) + "\n")

outFile.close()

