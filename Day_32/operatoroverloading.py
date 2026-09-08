#+-*/**%==><>=<=
'''class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __truediv__(self,other):
        return self.n/other.n
    def __floordiv__(self,other):
        return self.n//other.n
    def __mod__(self,other):
        return self.n%other.n
    def __pow__(self,other):
        return self.n**other.n
    def __eq__(self,other):
        return self.n==other.n
    def __nq__(self,other):
        return self.no!=other.n
    def __gt__(self,other):
        return self.n>other.n
    def __ge__(self,other):
        return self.n>=other.n
    def __lt__(self,other):
        return self.n<other.n
    def __le__(self,other):
        return self.n<=other.n

n1 =number(20)
n2 =number(10)
        
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1%n2)
print(n1**n2)
print(n1==n2)
print(n1!=n2)
print(n1>n2)
print(n1>=n2)
print(n1<n2)
print(n1<=n2)
'''

class user:
    def __init__(self,name,email,phone,password):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password

    def register(self):
        if not self.name:
            return "Registration failed: name is reguired" 
        if not self.email:
            return "Rgistration faild: email is required"
        if not self.phone:
            return "Registration failed: phone is required"
        if not self.password:
            return "REgistartion failed: password is required"
        return "Registration successfull"   

user1=user(name='sai', email='sai@gmail.com',phone='21324884',password='sa@12334')
print(user1.register())
user2=user(name='kowshik', email='',phone='21324884',password='sa@12334')
print(user2.register())