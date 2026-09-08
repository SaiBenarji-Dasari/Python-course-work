# int, float, str, tuple, bool ----> this are inside and outside will change output..
# list, set, dict ----> this are comes same inside and ouside the ouput..

def display(n):
    n[5]=6
    print('Inside:',n)
n={1:2,3:4}
display(n)
print('Outside:',n)   