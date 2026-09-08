'''
def data():
    a=['1..100','101..200','201..300','301..400','401..500','501..600']
    for i in a:
        yield i
reels = data()

while True:
    status = input('[c]ontinue or [e]xist:')
    if status=='c':
        print(next(reels))
    else:
        break    


def even():
    i=0
    while True:
        i+=2
        yield i
n=20
output=even()
for i in range(n):
    print(next(output))


def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

n=12       
res=factors(n)
for i in res:
    print(i)            
'''

def checkprime(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
def prime(n):
    for i in range(2,n+1):
        if checkprime(i):
            yield i
n=10
out=prime(n)
for i in out:
    print(i)            

