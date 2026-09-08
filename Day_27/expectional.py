'''try:
    #a=int(input())
    k={1:22,4:55}
    print(k[14])
    l=[22,644]
    print(1[10])
    print(10/0)
    print('1'+1)
#except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    #print('Error occured:',e)
except Exception as e:
    print('Error occured:',e)    

else:
    print('error free program')
finally:
    print('end the program')            
'''
try:
    a=int(input('Enter the amount: '))
    b=500
    if a<0:
         raise Exception("Amount needs to possitive")
except Exception as e:
      print("Error occured:",e)
else:
     print("Error free program")
finally:
     print("End the program")            