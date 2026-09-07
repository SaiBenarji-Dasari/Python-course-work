Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'python programming'
len(c)
18
ord('p')
112
ord('a')
97
ord('0')
48
ord(65)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(65)
TypeError: ord() expected string of length 1, but int found
chr(65)
'A'
chr(30)
'\x1e'
chr(75)
'K'
\
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
a = 'sai benarji
SyntaxError: unterminated string literal (detected at line 1)
a = 'sai benarji'
a
'sai benarji'
c.upper()
'PYTHON PROGRAMMING'
a.upper()
'SAI BENARJI'
a.lower()
'sai benarji'
a.title()
'Sai Benarji'
a.capitalize()
'Sai benarji'
c.swapcase()
'PYTHON PROGRAMMING'
a.swapcase()
'SAI BENARJI'
a,casefold()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a,casefold()
NameError: name 'casefold' is not defined
a.casefold()
'sai benarji'
a.center(70,'-')
'-----------------------------sai benarji------------------------------'
c.ljust(60,'-')
'python programming------------------------------------------'
a.rjust(60,'-')
'-------------------------------------------------sai benarji'
'11'.zfill(3)
'011'
a.find('i)
       
SyntaxError: unterminated string literal (detected at line 1)
a.find('i')
       
2
a.find('b')
       
4
c.rfind('a')
       
12
a.index('i')
       
2
a.rindex('a')
       
7
a
       
'sai benarji'
c.count('s')
       
0\
a.count('a')
       
2
a
       
'sai benarji'
a.replace('i','*')
       
'sa* benarj*'
a.replace('sai','dasari')
       
'dasari benarji'
a.maketrans('aeiou','@')
       
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.maketrans('aeiou','@')
ValueError: the first two maketrans arguments must have equal length
a.maketrans('aeiou','@@@@@')
       
{97: 64, 101: 64, 105: 64, 111: 64, 117: 64}
a.translate(a.maketrans('aeiou','@@@@@'))
       
's@@ b@n@rj@'
's@@ b@n@rj@'
       
's@@ b@n@rj@'
a
       
'sai benarji'
a.split()
       
['sai', 'benarji']
['sai', 'benarji'].split()
       
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ['sai', 'benarji'].split()
AttributeError: 'list' object has no attribute 'split'
'sai', 'benarji'.split()
       
('sai', ['benarji'])
'sai', 'benarji'.split(',')
       
('sai', ['benarji'])
'sai', 'benarji'.split('-')
       
('sai', ['benarji'])
KeyboardInterrupt
'sai', 'benarji'.rsplit()
       
('sai', ['benarji'])
a.rsplit()
       
['sai', 'benarji']
a.splitlines()
       
['sai benarji']
s ='''
dasari
sai
benarji'''
       
s
       
'\ndasari\nsai\nbenarji'
s.splitlines()
...        
['', 'dasari', 'sai', 'benarji']
>>> ''.join(['', 'dasari', 'sai', 'benarji'])
...        
'dasarisaibenarji'
>>> 'dasarisaibenarji'
...        
'dasarisaibenarji'
>>> '-'.join(s)
...        
'\n-d-a-s-a-r-i-\n-s-a-i-\n-b-e-n-a-r-j-i'
>>> s.partition(',')
...        
('\ndasari\nsai\nbenarji', '', '')
>>> w =  'the, do, there'
...        
>>> w.partition(',')
...        
('the', ',', ' do, there')
>>> a.strip()
...        
'sai benarji'
>>> z ='        sai
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> z ='        sai'
...        
>>> z.strip()
...        
'sai'
>>> z.lstrip()
...        
'sai'
>>> z.rstrip()
...        
'        sai'
>>> t = 'Hi 
KeyboardInterrupt
>>> t = 'Hii 😜'
...        
>>> t.encode()
...        
b'Hii \xf0\x9f\x98\x9c'
>>> t.decode()
...        
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'Hii \xf0\x9f\x98\x9c'.decode()
...        
'Hii 😜'
