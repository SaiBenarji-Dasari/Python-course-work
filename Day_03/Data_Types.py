Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
count =10
count
10
type(count)
<class 'int'>
a = 10.5
a
10.5
type(a)
<class 'float'>
b = 2+5s
SyntaxError: invalid decimal literal
c = 3+8j
c
(3+8j)
type(c
     )
<class 'complex'>
b = 4+5k
SyntaxError: invalid decimal literal
>>> s = 'sai'
>>> s
'sai'
>>> type(s)
<class 'str'>
>>> l = []
>>> l = list()
>>> type(l)
<class 'list'>
>>> l = {2,1,21,'asdykj',"wsdsww",(1,2)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> l = [2,22,55,'wdawdqwf',(12e43qr)]
SyntaxError: invalid decimal literal
>>> l = [1,2,3]
>>> l
[1, 2, 3]
>>> t = [1,2,3,bb,'sai']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t = [1,2,3,bb,'sai']
NameError: name 'bb' is not defined
>>> t = [1,2,3,d'sai']
SyntaxError: invalid syntax
>>> t = [1,2,3,d,'sai']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t = [1,2,3,d,'sai']
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> t = [1,2,3,"d",'sai']
>>> t
[1, 2, 3, 'd', 'sai']
>>> type(t)
<class 'list'>
>>> t = (1,2,3,'d',"sai")
>>> t
(1, 2, 3, 'd', 'sai')
>>> type(t)
<class 'tuple'>
>>> s = {1,2,2,"sai",3,3,44,5}
>>> s
{1, 2, 3, 5, 44, 'sai'}
>>> type(s)
<class 'set'>
>>> d = (1:22,2:33,3:44)
SyntaxError: invalid syntax
>>> d = {1:22,2:33,3:44}
>>> d
{1: 22, 2: 33, 3: 44}
>>> type(d)
<class 'dict'>
>>> bool(d)
True
