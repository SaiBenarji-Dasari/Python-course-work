'''i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

i=2
while i<=100:
    print(i ,end=',')
    i+=2

s="SAI BENARJI" 
i=len(s)-1
while i>=0:
    print(s[i], end='')
    i-=1   

a=[1,2,0,2,0,3,4,1,5,0,4,7,8,1,0,99,27,9]
while 0 in a:
    a.remove(0)
print(a)   

data={}
total =0
while True:
    product=input("Enter the product (for exit): ")
    if product=='exit':
        break
    price=int(input('Enter the price: '))
    total+=price
    data[product]=price
print(data)
print('TOtal:',total)
'''

i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("End the lopp")