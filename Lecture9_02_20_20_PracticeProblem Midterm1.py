# Practice problem 12 from midterm 1
'''
def vowel_tracker(words):
    vowels = 'aeiouAEIOU'
    beginCount = 0
    endCount = 0
    for string in words:
        if string[0]  in vowels:
            beginCount += 1
        if string[-1] in vowels:
            endCount += 1
    return [beginCount, endCount] 

advice = ['And','this','above','all']
print(vowel_tracker(advice))
'''
'''
# Practice problem 12 from midterm 2
def getDivergent(words):
    isDivergent = 0
    isNotDivergent = 0
    for string in words:
        if string[0] == string [-1]:
            isDivergent += 1
        if string[0] != string [-1]:
            isNotDivergent += 1
    return [isDivergent, isNotDivergent]

advice = ['the', 'secret', 'to', 'a', 'better', 'health', 'is', 'exercise']
print(getDivergent(advice))
'''
# Practice problem 13 from midterm 2
def printLines(line):
    repeat =  (int(input("Number of repetitions? ")))
    for i in range(repeat):
        print(line)
    return repeat

count = printLines('#####')
