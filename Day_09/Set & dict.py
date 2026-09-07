Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s
NameError: name 's' is not defined
s=()
type(s)
<class 'tuple'>
set()
set()
s=set()
s
set()
s.add(22)
s.add(23.2)
s.add(2+3)
s
{5, 22, 23.2}
s={1,1,1,1,11}
s
{1, 11}
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True
a
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}<a
False
{1, 2, 3, 4, 5}<=a
True
b
{9, 3, 5, 7}
a.isdijoint(b)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.isdijoint(b)
AttributeError: 'set' object has no attribute 'isdijoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issubset(a)
True
a
{1, 2, 3, 4, 5}
5 in a
True
a.issuperset(b)
False
7 in a
False
8 not in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.update({10,20,30})
a
{1, 2, 3, 4, 5, 10, 12, 20, 30}
a.pop()
1
a.pop()
2
a,remove(12)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a,remove(12)
NameError: name 'remove' is not defined
a.remove(12)
a
{3, 4, 5, 10, 20, 30}
a.discart(3)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.discart(3)
AttributeError: 'set' object has no attribute 'discart'. Did you mean: 'discard'?
a.discard(3)
a
{4, 5, 10, 20, 30}
a.discard({4,5})
a
{4, 5, 10, 20, 30}
a.clear()
a
set()
a={0,1,2,3,'sai',-22,0.2,}
len(a)
7
all(a)
False
any (a)
True
a = frozenset({1,22,30,44})
a
frozenset({1, 44, 22, 30})
a.ad(11)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.ad(11)
AttributeError: 'frozenset' object has no attribute 'ad'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'c1' ,'k2 : 'c2' ,'k3' : 'c3'}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'a':1, 'b':2, 'c':3}
   
d
   
{'a': 1, 'b': 2, 'c': 3}
id(d)
   
2709537587072
d['5']=d
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}}
d[12.3]='flt'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt'}
d[2+3j]='com;
   
SyntaxError: unterminated string literal (detected at line 1)
d[2+3j]='com'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com'}
d['str']='string'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com', 'str': 'string'}
d[(1,2,3)]='tuple'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3): 'tuple'}
d={}
...    
>>> d[1]=1
...    
>>> d[2]=2
...    
>>> d[3]=3
...    
>>> d[5]=5
...    
>>> d[6]=2+3j
...    
>>> d[7]='str'
...    
>>> d[8]=(1,2,3)
...    
>>> d
...    
{1: 1, 2: 2, 3: 3, 5: 5, 6: (2+3j), 7: 'str', 8: (1, 2, 3)}
>>> 1 in d
...    
True
>>> 9 in d
...    
False
>>> 10  not in d
...    
True
>>> 'str' in d
...    
False
>>> d[8]
...    
(1, 2, 3)
>>> d.get(1)
...    
1
>>> d.get(9,'key is not present')
...    
'key is not present'
>>> d.get(7,'key is not present')
...    
'str'
>>> d[5]=10
...    
>>> d
...    
{1: 1, 2: 2, 3: 3, 5: 10, 6: (2+3j), 7: 'str', 8: (1, 2, 3)}
>>> d[6]=100
...    
>>> d
...    
{1: 1, 2: 2, 3: 3, 5: 10, 6: 100, 7: 'str', 8: (1, 2, 3)}
