Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList = [2,2.5,True,"hello",[5,'hi']]
>>> len[myList]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len[myList]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(myList)
5
>>> myList[-1]
[5, 'hi']
>>> myList[3][0]
'h'
>>> myList[-1][-1]
'hi'
>>> myList[0,2]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    myList[0,2]
TypeError: list indices must be integers or slices, not tuple
>>> myList[0;2]
SyntaxError: invalid syntax
>>> myList[0:2]
[2, 2.5]
>>> myList[10:20]
[]
>>> myList[10]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    myList[10]
IndexError: list index out of range
>>> 