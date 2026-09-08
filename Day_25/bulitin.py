import sys
#print(sys.path)
 
#print(sys.version)
'''print('start')
sys.exit()
print('end')


import platform
print(platform.system())
print(platform.release())
print(platform.processor())


import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,6))

print(math.ceil(10.00001))
print(math.ceil(11.00000))
print(math.ceil(11.6))
print(math.ceil(12.0000))
print(math.ceil(13.99999))



print(math.floor(10.00001))
print(math.floor(11.00000))
print(math.floor(11.6))
print(math.floor(12.0000))
print(math.floor(13.99999))



print(math.fabs(-20))
print(math.factorial(5))
print(math.gcd(5,25))
print(math.log(2,2))
print(math.sin(20))
print(math.cos(20))
print(math.tan(20))
print(math.degrees(20))
print(math.radians(20))


import random
random.seed(5)
print(random.randint(1,9))
print(random.randint(10,30))
print(random.random())
print(random.uniform(1,6))

l=['s','A','I']
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)



from collections import Counter
s='Sai Benarji'
m= 'this is that is that this is'.split()
l=[1,2,31,1,1,4,5,6,7,89,999,]
print(Counter(s))
print(Counter(l))
print(Counter(m))

from collections import defaultdict
s='Sai Benarji'
m= 'this is that is that this is'.split()
l=[1,2,31,1,1,4,5,6,7,89,999,]

d= defaultdict(int)
for i in s:
    d[i]+=1
print(d)


from collections import defaultdict,Counter,deque

l=deque([])
l.append(10)
l.append(30)
l.append(20)
l.popleft()
l.popleft()
l.append(70)
l.append(50)
l.popleft()

print(l)


from collections import defaultdict,Counter,deque

l=deque([])
l.appendleft(10)
l.appendleft(30)
l.appendleft(20)
l.pop()
l.pop()
l.appendleft(70)
l.appendleft(50)
l.pop()

print(l)

'''

from itertools import combinations, permutations

r1=list(combinations('abc',2))
r2=list(permutations('abc',2))

print([''.join(i) for i in r1])
print([''.join(i) for i in r2])