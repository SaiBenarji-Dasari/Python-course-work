'''
# position arduments
def display(name,email,password):
    print(f'name:  {name}')
    print(f' email:  {email}')
    print(f'passwoard:  {password}')
  
display('sai','sai@gmail.com','Sai@123')
display('sai@123','sai@gmail.com','sai')
display('sai@gmail.com','sai@123','sai')

#key word argument  
def display(name,email,password):
    print(f'name:  {name}')
    print(f' email:  {email}')
    print(f'passwoard:  {password}')

display(name='sai',email='sai@gmail.com',password='Sai@123')
display(password='sai@123',email='sai@gmail.com',name='sai')
display(email='sai@gmail.com',password='sai@123',name='sai')

# default arguments
def display(name,email='enter mail',password=' '):
    print(f'name:  {name}')
    print(f' email:  {email}')
    print(f'passwoard:  {password}')

display(name='sai',email='sai@gmail.com',password='Sai@123')
display(password='sai@123',name='sai')
display(email='sai@gmail.com',name='sai')

# vairable arguments
def display(*names):
    print(names)
display('sai')
display('sai','benarji')
display('sai','benarji','dasari')    
'''
# key word variable arguments
def display(**product):
    print(product)
display(bag=400)
display(bag=4000,book=30)
display(bag=400,book=30,bottle=200)    