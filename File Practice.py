#1 open files
inputFile = open("scores.txt", 'r') # mode = 'r', 'w'

#2 process the file
#loop through a file(a file is collection of lines)
#for line in inputFile:
#   print(line, end = "")
#    tokens = line.split()
#    print(tokens[0])

#2 readlines()
#lineList = inputFile.readlines()
#for line in lineList:
#    print(lineList)
    
#3 read()
#content = inputFile.read()
#allWords = content.split()
#print(allWords)

#4 readLine()
header = inputFile.readline()
print(header)
allWords = inputFile.read().split()
print (len(allWords))

# close the file
inputFile.close()
