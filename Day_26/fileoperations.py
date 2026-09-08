'''
file=open('pfs.63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()


with open('pfs.63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
file.close()
'''

'''
with open('pfs.63.txt','w') as file:
    file.write('What are you doing')
    '''

'''with open('my sql.text','w') as file:
    file.write('css,Dql,SSS')
    '''

'''with open('pfs.63.txt','a') as file:
    file.write('Right Now')
'''
'''with open('pfs.63.txt','a+') as file:
    file.write('Ok Carry On')
    file.seek(0)
    print(file.read())
'''
with open('pfs.63.txt','w+') as file:
    file.write('Ok Carry On')
    file.seek(0)
    print(file.read())