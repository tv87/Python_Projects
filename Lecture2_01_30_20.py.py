Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('hello')
hello
>>> print ("Hello")
Hello
>>> print "hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> print ("Hello " + "CS100")
Hello CS100
>>> "hello" + "CS100"
'helloCS100'
>>> 'hello' + 'CS100'
'helloCS100'
>>> msg = "Hello"
>>> msg *5
'HelloHelloHelloHelloHello'
>>> len(msg)
5
>>> "he" in msg
False
>>> "He" in msg
True
>>> "CS100" not in msg
True
>>> msg[0]
'H'
>>> msg[-3]
'l'
>>> msg[-33]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    msg[-33]
IndexError: string index out of range
>>> msg[0]
'H'
>>> msg[-0]
'H'
>>> msg[-1]
'o'
>>> len(msg)
5
>>> msg[74]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    msg[74]
IndexError: string index out of range
>>> message = "hi everyone how are you quickly count the last character in the string"
>>> len(message)
70
>>> length = len(message)
>>> last = len(message) - 1
>>> print(message[last])
g
>>> print(message(len(message) -1))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(message(len(message) -1))
TypeError: 'str' object is not callable
>>> print(message[len(message) -1])
g
>>> message[-1]
'g'
>>> message[0,-2]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    message[0,-2]
TypeError: string indices must be integers
>>> message[0,2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    message[0,2]
TypeError: string indices must be integers
>>> ''
''
>>> message[0:2]
'hi'
>>> message[3:7]
'ever'
>>> message[-4:-1]
'rin'
>>> message[-4:0]
''
>>> message[:2]
'hi'
>>> message[-4:]
'ring'
>>> message[:]
'hi everyone how are you quickly count the last character in the string'
>>> message[0] = "H"
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    message[0] = "H"
TypeError: 'str' object does not support item assignment
>>> message.capitalize()
'Hi everyone how are you quickly count the last character in the string'
>>> message
'hi everyone how are you quickly count the last character in the string'
>>> first = "John"
>>> last = "Swity"
>>> firstName = ""
>>> print(first(0) + first(-1))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(first(0) + first(-1))
TypeError: 'str' object is not callable
>>> print(first[0] + first[-1])
Jn
>>> print(first[0] + first[-1} + last[0] + last[-1])
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> print(first[0] + first[-1] + last[0] + last[-1])
JnSy
>>> 
>>> firstName = input {"What is yuor first name?"}
SyntaxError: invalid syntax
>>> >>> firstName = input ("What is yuor first name?")
SyntaxError: invalid syntax
>>> >>> firstName = input ["What is yuor first name?"]
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> >>> firstName = input ('What is yuor first name? "')
SyntaxError: invalid syntax
>>> firstName = input ("What is your first name? ")
What is your first name? 
>>> Tej
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    Tej
NameError: name 'Tej' is not defined
>>> firstName = input ("What is your first name? ")
What is your first name? Tej
>>> print (firstName[0] + firstName[-1])
Tj
>>> message = "hello"
>>> message == "Hello"
False
>>> "This" >= "That"
True
>>> "zoo" > "bear"
True
>>> "book" > "bookcase"
False
>>> myList = [2,2.5,True, "Hello"]
>>> type(myList)
<class 'list'>
>>> myList + [1,2,3,4,5]
[2, 2.5, True, 'Hello', 1, 2, 3, 4, 5]
>>> myList + 200
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    myList + 200
TypeError: can only concatenate list (not "int") to list
>>> myList + "Hello"
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    myList + "Hello"
TypeError: can only concatenate list (not "str") to list
>>> myList + ["Hello"]
[2, 2.5, True, 'Hello', 'Hello']
>>> myList *2.5
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    myList *2.5
TypeError: can't multiply sequence by non-int of type 'float'
>>> myList * 3
[2, 2.5, True, 'Hello', 2, 2.5, True, 'Hello', 2, 2.5, True, 'Hello']
>>> len(myList)
4
>>> 2.5 in myList
True
>>> "he" in myList
False
>>> "hello" not in myList
True
>>> myList [1]
2.5
>>> myList[0]
2
>>> myList[200]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    myList[200]
IndexError: list index out of range
>>> slice myList
SyntaxError: invalid syntax
>>> myList [0:2]
[2, 2.5]
>>> myList[-2:]
[True, 'Hello']
>>> myList[-1:1]
[]
>>> myList[20:100]
[]
>>> # slice is a part of the list
>>> 
>>> ///////////ll
SyntaxError: invalid syntax
>>> myList[-1][-1:]
'o'
>>> # myList position operator followed by a slice operator
>>> 