'''
for i in range(1,10):
    if i ==15:
        break
    print(i)
else:
    print('End of the loop')

pin=123
for _ in range(5):
    epin=int(input('Enter the number: '))
    if pin==epin:
        print("unlock the phone")
        break
        
    else:
        print('invalid pin')    
else:
    print('Try again after 30 sec')

a=int(input('Enter the number'))
print("factors: ", end=' ')
for i in range(1,a+1):
    if a%i==0:
        print(i,end=' ')

n=int(input('Enter the number: '))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime number")
else:
    print("Not Prime Number")            
''' 

n=int(input('Enter the number: '))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not prime number")
        break
else:
    print('prime number')    