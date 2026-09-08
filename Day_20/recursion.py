'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)    

def display(n):
    if n<1:
        return
    print(n)
    display(n-1)
display(10)    

def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(8))

def product(n):
    if n==1:
        return 1
    return n*product(n-1)
print(product(5))

def display(ind):
    if ind==len(s):
        return
    display(ind+1)
    print(s[ind], end='')
s='SAI'
display(0)

def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)
s="SAI"
display(1)    

def display(ind,w):
    if ind>len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)

s="Sai Benarji"
display(0,10)

def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)  
n=987654             
display(n)           
'''


    