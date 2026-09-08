'''
l = [updating for loop]
l = [updating for loop if cond]
l = [upd1 if cond else upd2 for loop]
l = [upd for loop1 for loop2]
l = [upd for loop1 for loop2 if cond] 

l=[int(input(f"Enter the number - {i+1}: ")) for i in range(10)]

print(l)

names = {input(f"Enter the name-{i+1}: "): 
         int(input("Enter the marks: "))
          for i in range(5)}
print(names)
'''



res = {i:i*i for i in range(1,11)}
print(res)