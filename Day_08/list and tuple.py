Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = [1,2,3,55,4]
l
[1, 2, 3, 55, 4]
id(l)
2373068285312
l.append(27)
l
[1, 2, 3, 55, 4, 27]
l.append(9)
l
[1, 2, 3, 55, 4, 27, 9]
id(l)
2373068285312
l.insert(0,0)
l
[0, 1, 2, 3, 55, 4, 27, 9]
l.append([5,12])
l
[0, 1, 2, 3, 55, 4, 27, 9, [5, 12]]
lremove(5,12)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lremove(5,12)
NameError: name 'lremove' is not defined
l.remove(5,12)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.remove(5,12)
TypeError: list.remove() takes exactly one argument (2 given)
l.pop()
[5, 12]
l
[0, 1, 2, 3, 55, 4, 27, 9]
l.extand([5,12])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.extand([5,12])
AttributeError: 'list' object has no attribute 'extand'. Did you mean: 'extend'?
l.extend([5,12])
l
[0, 1, 2, 3, 55, 4, 27, 9, 5, 12]
id(l)
2373068285312
l[-1]
12
l.pop(4)
55
l
[0, 1, 2, 3, 4, 27, 9, 5, 12]
l.remove(55)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    l.remove(55)
ValueError: list.remove(x): x not in list
l.remove(4)
l
[0, 1, 2, 3, 27, 9, 5, 12]
del l(2)
SyntaxError: cannot delete function call
del l[2]
l
[0, 1, 3, 27, 9, 5, 12]
max(l)
27
min(l)
0
sorted(l)
[0, 1, 3, 5, 9, 12, 27]
l
[0, 1, 3, 27, 9, 5, 12]
l.reverse()
l
[12, 5, 9, 27, 3, 1, 0]
l.sort()
l
[0, 1, 3, 5, 9, 12, 27]
l.sort(reverse=True)
l
[27, 12, 9, 5, 3, 1, 0]
sum(l)
57
\
l =[1,2,3]
m =[1,2,3]
l
[1, 2, 3]
n =l
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m =l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
>>> l
[1, 2, 3, 4]
>>> all(0,'',[],(),set(),{},false)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    all(0,'',[],(),set(),{},false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> KeyboardInterrupt
>>> all([0,'',[],(),set(),{},False])
False
>>> allall([1,'',[],(),set(),{},False])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    allall([1,'',[],(),set(),{},False])
NameError: name 'allall' is not defined
>>> all([1,'',[],(),set(),{},False])
False
>>> any([1,'',[],(),set(),{},False])
True
>>> l
[1, 2, 3, 4]
>>> l.index(4)
3
>>> l.count(1)
1
>>> l
[1, 2, 3, 4]
>>> [[1,2,3,4], [5,6,7,8]]
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
1
\
>>> l =[[1,2,3,4], [5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[0][-1]
4
>>> 1[-1][-2]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    1[-1][-2]
TypeError: 'int' object is not subscriptable
>>> 1[-1][0]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    1[-1][0]
TypeError: 'int' object is not subscriptable
>>> l[1][0]
5
