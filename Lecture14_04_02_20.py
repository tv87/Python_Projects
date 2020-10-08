# Problem 1
'''
def readAndWrite(name1, name2):
    inFile = open(name1, 'r')
    outFile = open(name2, 'w')

    # go through each line in input file, find the number of words and
    #    write num to output file
    for line in inFile:
        # line is a string, split it
        words = line.split()
        numWords = len(words)
        outFile.write(str(numWords) + "\n")

    inFile.close()
    outFile.close()
   
readAndWrite("data.txt", "output.txt")
'''

# Problem 2
'''
def initVowelCount(inFile, outFile):
    inF = open(inFile)
    outF = open(outFile,'w')
    vowels = 'aeiouAEIOU'

    linesInFile = inF.readLines()
    for line in linesInFile:
        if line == "\n":
            outF.write("\n")
            continue
        wordsList = line.split()
        for word in wordsList:
            if word[0] in vowels:
                count += 1
        outF.write(str(count) + "\n")
    inF.close()
    outF.close()

initVowelCount('run.txt', 'runInitVowel.txt')
'''

# Problem 3
def wordFreq(inFile, outFile):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')

    content = inF.read() # content contains the whole content of the file in one string
    wordsList = content.lower().split()
    d ={}
    for word in wordsList:
        d[word] = wordsList.count(word)

    for key in d:
        outF.write(key + " " + str(d[key])+ '\n')

    inF.close()
    outF.close()

wordFreq('data.txt', 'funWordFreq.txt')








