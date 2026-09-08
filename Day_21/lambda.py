'''
greater=lambda a,b:a if a>b else b
print(greater(12,30))
print(greater(50,70))
print(greater(40,20))
print(greater(16,26))

wish=lambda name: f'Welcome to the course {name}'

print(wish('Sai'))
print(wish('Benarji'))
print(wish('kowshik'))

iseven=lambda n: 'even'if n%2==0 else 'odd'

print(iseven(45))
print(iseven(27))
print(iseven(9))

avg=lambda a,b,c: (a+b+c)/3

print(avg(4,5,6))
print(avg(27,9,5))


domain=lambda mail:(mail.split('@')[-1]).split('.')[0]

print(domain('sai@gamil.com'))
print(domain('sai@otlook.com'))


gst=lambda price: price+price*0.18
print(gst(5000))
print(gst(2000))
print(gst(1000))

prices=[12,33,22,410,555]
a=list(map(lambda price: price+price*0.18,prices))
print(a)

na=['sai','benarji','dasari','kowshik']
b=list(map(lambda name:name.title(),na))
print(b)


a=[100,200,122,301,21,55,451]
b=list(map(lambda price:price-price*0.3,a))
print(b)


a=[100,200,122,301,21,55,451]
b=list(filter(lambda price:price>200,a))
print(b)

a=[100,200,122,301,21,55,451]
b=list(filter(lambda price:price%2==0,a))
print(b)

names={'benarji','asdfb','msndhkjqeh','aad'}
a=list(filter(lambda name:len(name)>5,names))
print(a)

from functools import reduce
a=[12,3232,4565,45,2123]
b=reduce(lambda sum,i:sum+i,a)
print(b)

from functools import reduce
n=['adaSDAEWF','AFSDRDR','arrtdtjvmm','vxvvbvchhj']
a=reduce(lambda a,i:a+' '+i,n)
print(a)
p={'sugar':60,'oil':100,'salt':30}
print(dict(sorted(p.items())))
print(dict(sorted(p.items(),reverse=True)))

print(dict(sorted(p.items(),key=lambda i:i[1] )))
print(dict(sorted(p.items(),reverse=True,key=lambda i:i[1] )))
'''
a=int(input('Enter the Number:'))
senior_citizen=eval(input())==True
if  0 <= a <= 100:
    bill=a*1.5
elif 101 <= a <= 200:
    bill=a*2.5
elif 201 <= a <= 300:
    bill=a*4
elif  500 <= a <= 5000:
    bill=a*6
if senior_citizen:
    bill=bill-(bill*10/100)
if a>=800:
    bill=bill+(bill*0.05)
print(int(bill))