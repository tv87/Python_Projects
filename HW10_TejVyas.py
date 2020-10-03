# Tej Vyas
# CS 100 2020S Section 006
# HW 10, March 31, 2020

# Problem 1
def initialLetterCount(wordList):
    d = {}
    for word in wordList:
        firstLetter = word[0]
        if firstLetter not in d:
            d[firstLetter] = 1
        else:
            d[firstLetter] += 1
    return d
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))


# Problem 2
def initialLetters(wordList):
    d ={}
    repeatedWords = []
    for word in wordList:
        firstLetter = word[0]
        if word not in d:
            d[firstLetter] = [word]
        else:
            repeatedWords.append(word)
    return d
print(initialLetters(horton))

# Problem 3
def shareALetter(wordList):
    d ={}
    for word in wordList:
        if word not in d:
            repeatedWords = []
            for letter in word:
                for k in wordList:
                    if letter in k:
                        if k not in repeatedWords:
                            repeatedWords.append(k)
        d[word] = repeatedWords
    return d
print(shareALetter(horton))
