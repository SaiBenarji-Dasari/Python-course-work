'''
def display(n):
    n=n+10
    print('Inside:',n)
n=10
display(n)
print('inside:',n)    

def display():
    print('outside:',n)
n=10
display()
print("Inside:",n)

def display():
    n=10
    print('Inside',n)
display()
print('Outside:',n)    

def display():
    global n
    n=n+10
    print("Inside:",n)
n=10
display()
print('Outside:',n) 

def display(n):
    n='pfs'
    print('update course:',n)
n='jfs'
display(n)
print('final course:',n)
'''
def display():
    n='JFS'
    def update():
        nonlocal n
        n="PFS"
        print("Update Course:",n)
    update()
    print("Final Course:", n)    
display()    
# if we use a variables on bulit in function it changes into function so the code will get error 