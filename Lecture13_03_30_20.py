'''
def wordLengths(text):
    wordsList = text.split()
    d = {}
    for word in wordsList:
        length = len(word)
        if length not in d:
            d[length] = 1
        else:
            d[length] += 1
    return d

text = 'Go to heaven for the climaate hell of the company'
print(wordLengths(text))
'''
'''
def lengthDictionary(line):
    wordsList = line.split()
    d = {}
    length = len(word)
    for word in wordsList:
        length = len(word)
        if length not in d:
            d[length] = [word]
        else:
            d[length].append(word)
    return d
    
print(lengthDictionary("it is what it is"))
'''
'''
def initialDict(text):
    d = {}
    words = text.split()
    for word in words:
        firstLetter = word[0].lower()
        if firstLetter not in d:
            d[firstLetter] = [word]
        else:
            d[firstLetter].append(word)
    return d
print(initialDict("The Call of the Wild"))
'''

def analyzeAreaCodes(phones):
    d = {}

    for phoneNumber in phones:
        areaCode = phoneNumber[:3]
        if areaCode not in d:
            d[areaCode] = 1
        else:
            d[areaCode] += 1
    return d
phones = ['982-222-2222', '732-323-3232', '982-334-4444']
print(analyzeAreaCodes(phones))





























        
    
