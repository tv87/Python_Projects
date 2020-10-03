Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tej Vyas
>>> # CS 100 2020S Section 006
>>> # HW 01, January 30, 2020
>>> 
>>> # Exercise 5b
>>> age = 12
>>> week = 7
>>> 
>>> student = 37
>>> 
>>> # Exercise 5c
>>> weight = 133.4
>>> grade = 30.2
>>> miles = 60.2
>>> 
>>> # Excercise 5d
>>> speakSpanish = 'Hola'
>>> rock = 'stone'
>>> car = 'BMW'
>>> 
>>> # Exercise 1.1.1
>>> 
>>> print 'hello'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello')?
>>> # Exercise 1.1.2
>>> print('hello')
hello
>>> # Exercise 1.1.3
>>> print(2++2)
4
>>> 
>>> # Exercise 1.1.4
>>> print (001)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> # Exercise 1.1.5
>>> print (22)
22
>>> # Exercise 1.2.1
>>> 42*60
2520
>>> 2520 + 42
2562
>>> # Exercise 1.2.2
>>> 10/1.61
6.211180124223602
>>> # Exercise 1.2.3
>>> Avg pace = 42.7/6.21371
SyntaxError: invalid syntax
>>> Avg Pace = 42.7/6.21371
SyntaxError: invalid syntax
>>> Avg Pace = 0.621371
SyntaxError: invalid syntax
>>> # Exercise 2.1.1
>>> 42 = n
SyntaxError: cannot assign to literal
>>> # Exercise 2.1.2
>>> x = y = 1
>>> # Exercise 2.1.3
>>> print(2*2);
4
>>> # Exercise 2.1.4
>>> print(2*2).
SyntaxError: invalid syntax
>>> # Exercise 2.1.5
>>> a*b
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a*b
NameError: name 'a' is not defined
>>> # Exercise 2.2.1
>>> radius = 5
>>> print((4 * 3.14 * ((radius) * * 3))/3)
SyntaxError: invalid syntax
>>> # Exercise 2.2.2
>>> 0.6 * 24.95
14.969999999999999
>>> Cover_price = 0.6 * 24.95
>>> total_cost = (Cover_price) * 60 + (3 * 59 * 0.75))
SyntaxError: unmatched ')'
>>> total_cost = (Cover_price) * 60 + (3 * 59 * 0.75)
>>> Print (total_cost = (Cover_price) * 60 + (3*59*0.75))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    Print (total_cost = (Cover_price) * 60 + (3*59*0.75))
NameError: name 'Print' is not defined
>>> Traceback(most recent call last):
	
SyntaxError: invalid syntax
>>> print (total_cost)
1030.9499999999998
>>> 
>>> # Exercise 2.2.3
>>> left = (6 * 60 + 52) * 60
>>> easy_pace = (8 * 60 + 15) * 2
>>> tempo_pace = (7 * 60 + 12) *3
>>> finish = (left + easy_pace + tempo_pace) / (60 * 60.0)
>>> finishing = (left + easy_pace + tempo_pace) // (60 * 60)
>>> finish_minute = (finish - finishing) * 60
>>> print('Finish time was %d:%d' % (finish, finish_minute))
Finish time was 7:30
>>> 