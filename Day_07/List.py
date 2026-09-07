Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'string.py'
c.startswith('str')
True
c.startswith(python)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c.startswith(python)
NameError: name 'python' is not defined
c.startswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'SAI'.isupper()
True
c.isalpha()
False
c.isalnum()
False
>>> 'sai2005'.isalnum()
True
>>> 'sai.2005'.isalnum()
False
>>> '        '.isspace()
True
>>> 's        '.isspace()
False
\
>>> 'this is the title'.istitle()
False
>>> 'This Is The Title'.istitle()
True
>>> 'my_name'.isidentifier()
True
>>> 'my@name'.isidentifier()
False
>>> l = []
>>> l = list()
>>> l = [1,2,3,3,3+4,[1,2,34],'sai']
>>> l
[1, 2, 3, 3, 7, [1, 2, 34], 'sai']
>>> l = [1,2,3]
>>> l
[1, 2, 3]
>>> type(l)
<class 'list'>
>>> l = [1,2,3,4]
>>> m=[20,10,30]
\
>>> l+m
[1, 2, 3, 4, 20, 10, 30]
>>> m*3
[20, 10, 30, 20, 10, 30, 20, 10, 30]
>>> l
[1, 2, 3, 4]
>>> 1[3]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    1[3]
TypeError: 'int' object is not subscriptable
>>> l[3]
4
>>> l[-1]
4\
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
