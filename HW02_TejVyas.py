# Tej Vyas
# CS 100 2020S Section 006
# HW 02, February 3, 2020

# Question 1
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'),
             grades.count('D'), grades.count('F')]
print('Question #1')
print('grades: ', grades)
print()
print('frequency: ', frequency)
print()

# Question 2a
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print('Question #2a \ndog_breeds:', dog_breeds)

# Question 2b
herding_dogs = (dog_breeds[0:2])
print('\nQuestion #2b \nherding_dogs: ', herding_dogs)

# Question 2c
tiny_dogs = (dog_breeds[-1])
print('\nQuestion #2c \ntiny_dogs: ', tiny_dogs)

# Question 2d
isIn = 'Persion' in dog_breeds
print('\nQuestion #2d \nIs Persion in dog_breeds? \n', isIn)

