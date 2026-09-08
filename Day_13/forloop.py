'''
s='Sai Benarji'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i, s[i])

  a=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(a)):
    if a[i]%2==0:
        sum=sum+i
        print(i,a[i])
print(sum)       

n=int(input('Enter the number: '))
fact=1
for i in range(1,n+1):
    fact*=i
print(f'Factorial of {n} is {fact}')

data={}
n=int(input('Enter the no of students:'))
max_marks=0
for i in range(n):
    name=input('Enter the name of the student:')
    marks=int(input('Enter the marks of the student:'))
    if marks>max_marks:
        max_marks=marks
        data[name]=marks
print(data)
print('maximum marks:', max_marks)
'''
data={}
a=int(input('Enter the no of Products:'))
sum=0
for i in range(a):
    name=input('Enter the name of the Product:')
    price=int(input('Enter the price of the product:'))
    quantity=int(input('Enter the quantity of the product:'))
    total=price*quantity
    data[name]=total
    sum+=total
    data[name]=f'{price} * {quantity} = {total}'
print(data)
print('total amount:', sum)
