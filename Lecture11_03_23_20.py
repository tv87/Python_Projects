'''
for i in range(5):
    print(i, "hello")
'''

#set up your initial step
i = 0
#goal is to move counter from 0 - 4
# while counter has not reached 5
# while counter is less than 5
while i < 5:
    print(i, 'hello')
    i = i + 1 # changing i to get close to 5
    if i ==5:
        break
    if i % 2 == 1:
        continue

print ("End of my program")
