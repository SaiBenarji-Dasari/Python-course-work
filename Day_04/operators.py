Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
b = 20
a+b
30
a-b
-10
a*b
200
a/b
0.5
a//b
0
a%b
10
a**b
100000000000000000000
a
10
b
20
a,b
(10, 20)
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
n = 20
n += 10
n
30
n-=5
n
25
n/2
12.5
n//=2
n
12
n%=1
n
0
n*=2
n
0
n**=3
n
0
n=10
n
10
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%9==0 0r n%3==0
SyntaxError: invalid decimal literal
n%9==0 or n%3==0
False
n
10
n<5
False
notn<5
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    notn<5
NameError: name 'notn' is not defined
not n<5
True
# str, list, tuple, set, dirct
s='sai'
s in s
True
b in s
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b in s
TypeError: 'in <string>' requires string as left operand, not int
b not in s
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    b not in s
TypeError: 'in <string>' requires string as left operand, not int
s = 'benarji'
b in s
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b in s
TypeError: 'in <string>' requires string as left operand, not int
'b' in s
True
'z' in s
False
'w' not in s
True
l =[1,2,3,4]
'1' in l
False
1 in l
True
t =(1,2,3,4,5,6)
2 in t
True
9 not in t
True
s ={1,2,3,4,5,6,7}
1 in s
True
0 not in s
True
d = {'name':"sai",'age':"21"}
'name' in d
True
"sai" not in d
True
l = [1,2,3,4]
m=[1,2,3,4]
id(l)
2385282068352
id(m)
2385327749312
l is m
False
n = l
id(n)
2385282068352
n is l
True
l is not m
True
l is not m
True
l is not n
False
s = {1,2,3,4}
id(s)
2385327579744
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2385327579744
9&10
8
9|10
11
9^10
3
>>> 8>>3
1
>>> 8<<3
64
>>> ~6
-7
>>> ~1
-2
>>> ~0
-1
>>> a = 10
>>> b = 20.2
>>> c = 'SAI'
>>> print(a,b,c)
10 20.2 SAI
>>> print("a value is ",a)
a value is  10
>>> print('a value is' ,a,'| b value is',b,'| c value is',c,)
a value is 10 | b value is 20.2 | c value is SAI
>>> print(a,b,c)
10 20.2 SAI
>>> print(a,b,c,sep='')
1020.2SAI
>>> print(a,b,c,sep='\n')
10
20.2
SAI
>>> print(a,b,c,sep='\t')
10	20.2	SAI
>>> print(a,b,c,sep='\t',end ='@')
10	20.2	SAI@
>>> print(a,b,c,sep='\t',end = '\n\n')
10	20.2	SAI

>>> print(f'a={a} b={b} c={c}')
a=10 b=20.2 c=SAI
\
>>> print(f"a value is {a} |  b  value is
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"a value is {a} |  b  value is {b} | c value is {c}")
...       
a value is 10 |  b  value is 20.2 | c value is SAI
>>> print('a=%d b %f c=%s'%(a,b,c))
...       
a=10 b 20.200000 c=SAI
>>> print('a=%d b %.2f c=%s'%(a,b,c))
...       
a=10 b 20.20 c=SAI
>>> print('a= {}
...       
SyntaxError: unterminated string literal (detected at line 1)
