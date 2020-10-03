# Tej Vyas
# CS 100 2020S Section 006
# HW05, February 24, 2020

# Question 1
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY",
          "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER",
          "NOVEMBER", "DECEMBER"]
for i in range(len(months)):
    if months[i][0] == 'J':
       print(months[i])

# Question 2
for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
       print(i)

# Question 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for i in range(len(horton)):
    if horton[i] in vowels:
       print(horton[i])
