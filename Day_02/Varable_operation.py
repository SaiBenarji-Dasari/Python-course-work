Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=20
>>> a
10
>>> b
20
>>> a=10
>>> a,b,c,=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a
NameError: name 'a' is not defined
