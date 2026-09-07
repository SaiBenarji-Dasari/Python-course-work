Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
n = input()
n
n
'n'
name = input()
sai
name
'sai'
age = int(input())
21
age
21
a  input()
SyntaxError: invalid syntax
a = input()
21
a
'21'
n = input ("Enter the name:")
Enter the name: sai benarji
n
' sai benarji'
n.split
<built-in method split of str object at 0x0000026C99A217B0>
n.split
<built-in method split of str object at 0x0000026C99A217B0>
n.split()
['sai', 'benarji']
n = input('give name').split()
give name sai benarji
n
['sai', 'benarji']
s = input('enter the vlaues').split()
enter the vlaues1 2 3 3 3 4 4 5 5 5 6 6
s
['1', '2', '3', '3', '3', '4', '4', '5', '5', '5', '6', '6']
map(int,sw)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    map(int,sw)
NameError: name 'sw' is not defined. Did you mean: 's'?
\
map(int ,s)
<map object at 0x0000026C9B80E780>
list(map(int,s))
[1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6]
v = list(map(int,input().split()))
1 2 3 4 5 6 7 8 9
v
[1, 2, 3, 4, 5, 6, 7, 8, 9]
v = list(map(float,input().split()))
12 22.3 12 22 
v
[12.0, 22.3, 12.0, 22.0]
d = tuple(input('enter the vlaues').split())
enter the vlaues 1 2 3 44 55 7
d
('1', '2', '3', '44', '55', '7')
map(int,d)
<map object at 0x0000026C9B787D00>
tuple(map(int,d)
      1 2 2
      
SyntaxError: '(' was never closed
tuple(map(int,d))
      
(1, 2, 3, 44, 55, 7)
v = tuple(map(int,input().split()))
      
1 2 34 4
v
      
(1, 2, 34, 4)
b = list(map(float,input().split()))
      
1 2.3 3 4 4454  
b
      
[1.0, 2.3, 3.0, 4.0, 4454.0]
a,b = [1,2]
      
a
      
1
b
      
2
a,b(1,2)
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b(1,2)
TypeError: 'int' object is not callable
a,b =(1,2)
      
a
      
1
b
      
2
email, password= input('Enter the email and password:').split()
      
Enter the email and password:sai@gmail.com 22222
email
      
'sai@gmail.com'
password
      
'22222'
a,b,c= list(map(int,input().split()))
      
... 11 22 33 4556
... Traceback (most recent call last):
...   File "<pyshell#47>", line 1, in <module>
...     a,b,c= list(map(int,input().split()))
... ValueError: too many values to unpack (expected 3, got 4)
... a
... a,b,c= list(map(int,input().split()))
...       
... 41,22,55
... Traceback (most recent call last):
...   File "<pyshell#50>", line 1, in <module>
...     a,b,c= list(map(int,input().split()))
... ValueError: invalid literal for int() with base 10: '41,22,55'
... c,d,f= list(map(int,input().split()))
...       
... 
... Traceback (most recent call last):
...   File "<pyshell#51>", line 1, in <module>
...     c,d,f= list(map(int,input().split()))
... ValueError: not enough values to unpack (expected 3, got 0)
... e = eval(input())
...       
... e = eval(input())
... Traceback (most recent call last):
...   File "<pyshell#52>", line 1, in <module>
...     e = eval(input())
...   File "<string>", line 1
...     e = eval(input())
...              ^^^^^
... SyntaxError: invalid syntax. Did you mean 'not'?
... e = eval(input())
...       
... 1\
... Traceback (most recent call last):
...   File "<pyshell#53>", line 1, in <module>
...     e = eval(input())
...   File "<string>", line 1
...     1\
...      ^
... SyntaxError: unexpected character after line continuation character
... e = eval(input())
...       
... kuiuioll
... Traceback (most recent call last):
...   File "<pyshell#54>", line 1, in <module>
...     e = eval(input())
...   File "<string>", line 1, in <module>
...     __import__('idlelib.run').run.main(True)
... NameError: name 'kuiuioll' is not defined
... e = eval(input())
...       
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
