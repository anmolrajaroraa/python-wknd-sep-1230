Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> #class - blueprint
>>> #classes - integer, float, string, boolean, bytes
>>> id(a)
4333252048
>>> #10 - 0x433325 -> a
>>> hex(id(a))
'0x102482dd0'
>>> hex(id(b))
'0x102482f10'
>>> 
>>> #Number systems
>>> Binary - 0 and 1
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Binary - 0 and 1
NameError: name 'Binary' is not defined
>>> #Binary - 0 and 1   - singl line comment
>>> 
>>> 
>>> #Binary - 0 and 1
>>> #Octal numbers - 0 to 7
>>> #Decimal numbers - 0 to 9
>>> #Hexadecimal numbers - 0 to 9, 10, 11, 12, 13, 14, 15
>>> 
>>> 
>>> 
>>> #Hexadecimal numbers - 0 to 9, 10-a, 11-b, 12-c, 13-d, 14-e, 15-f
>>> 
>>> #121cf2132d
>>> 
>>> 
>>> 
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> type
<class 'type'>
>>> print
<built-in function print>
>>> print()  #function call

>>> #print(argument1, argument2 .... argument10)
>>> print('hello everyone')
hello everyone
>>> 
>>> 
>>> 
>>> 
>>> a= 10
>>> type(a)
<class 'int'>
>>> 
>>> #everything in python is an object
>>> 
>>> b = 20
>>> #IDLE
>>> 
>>> c = -20
>>> print(c)
-20
>>> c
-20
>>> a
10
>>> id(a)
4333252048
>>> x = id(a)
>>> x
4333252048
>>> hex(x)
'0x102482dd0'
>>> 
>>> hex(id(a)) #nested call
'0x102482dd0'
>>> 
>>> 
>>> 
>>> a = 10
>>> b = 20
>>> c = a +
SyntaxError: invalid syntax
>>> c = a + b
>>> 
>>> c = a + b
>>> print(c)
30
>>> print("Sum of a and b is 30")
Sum of a and b is 30
>>> print("Sum of a and b is" + c)   #string concatenation (joining)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print("Sum of a and b is" + c)   #string concatenation (joining)
TypeError: can only concatenate str (not "int") to str
>>> type(c)
<class 'int'>
>>> x = 'hello'
>>> type(x)
<class 'str'>
>>> str
<class 'str'>
>>> str()
''
>>> str(c)
'30'
>>> z = str(c)
>>> z
'30'
>>> type(z)
<class 'str'>
>>> print("Sum of a and b is" + str(c))   #type casting(conversion)
Sum of a and b is30
>>> print("Sum of a and b is " + str(c))
Sum of a and b is 30
>>> print("Sum of" + str(a) + "and" + str(b) + "is" + str(c))
Sum of10and20is30
>>> print("Sum of " + str(a) + " and " + str(b) + " is " + str(c))
Sum of 10 and 20 is 30
>>> 
>>> print("Sum of",a,"and",b,"is",c)
Sum of 10 and 20 is 30
>>> type(a)
<class 'int'>
>>> 
>>> print("Sum of {} and {} is {}")
Sum of {} and {} is {}
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 30
>>> 
>>> print("Sum of {} and {} is {}".format(c,a,b))
Sum of 30 and 10 is 20
>>> 
>>> 
>>> print("Sum of a and b is c")
Sum of a and b is c
>>> print("Sum of {a} and {b} is {c}")
Sum of {a} and {b} is {c}
>>> print(f"Sum of {a} and {b} is {c}")
Sum of 10 and 20 is 30
>>> 
>>> 
>>> #1
>>> print("Sum of " + str(a) + " and " + str(b) + " is " + str(c))
Sum of 10 and 20 is 30
>>> #2
>>> print("Sum of",a,"and",b,"is",c)
Sum of 10 and 20 is 30
>>> #3
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 30
>>> #4
>>> print(f"Sum of {a} and {b} is {c}")
Sum of 10 and 20 is 30
>>> 
>>> 
>>> a + b
30
>>> a - b
-10
>>> a * b
200
>>> a / b
0.5
>>> 5365/789
6.799746514575412
>>> #classic division - long division
>>> 
>>> 
>>> 5365//789
6
>>> #floor division
>>> 
>>> 
>>> 54 * 2
108
>>> 54 ** 2
2916
>>> 54 ** 3
157464
>>> 54 ** 4
8503056
>>> 54 ** 5
459165024
>>> 
>>> 
>>> input("What's your name: ")
What's your name: Anmol
'Anmol'
>>> 'Anmol'
'Anmol'
>>> 
>>> name = input("What's your name: ")
What's your name: Anmol
>>> print(name)
Anmol
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 10
Enter second number: 20
Sum of 10 and 20 is 1020
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 32
Enter second number: 23
Sum of 32 and 23 is 3223
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 76
Enter second number: 54
<class 'str'>
<class 'str'>
Sum of 76 and 54 is 7654
>>> 
>>> 
>>> 
>>> 10 + 20
30
>>> '10' + '20'
'1020'
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 32
Enter second number: 23
<class 'str'>
<class 'str'>
Sum of 32 and 23 is 3223
>>> 
>>> 
>>> 
>>> c = 20
>>> type(c)
<class 'int'>
>>> str(c)
'20'
>>> 
>>> c = '20'
>>> int(c)
20
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 64
Enter second number: 34
Sum of 64 and 34 is 98
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep-1230/input-fn.py ==
Enter first number: 645
Enter second number: 76
Sum of 645 and 76 is 721
Diff of 645 and 76 is 569
>>> 
