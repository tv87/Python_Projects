'''
Write a function uniqueWords() that takes one parameter called paragraph, a string containing words and whitespaces.
The funcion returns a list of all the distinct words in the paragraph

For example
paragraph:

it is what it is
python is a lot of fun

output:
['it', 'is', 'what', 'python', 'a', 'lot', 'of', 'fun']
'''
def uniqueWords(paragraph):
    wordsList = paragraph.split()
    unique = []
    for word in wordsList:
        if word not in unique:
            unique.append()
    return wordsList

para = "it is what it is. python is a lot of fun"
uniqueWords(para)

