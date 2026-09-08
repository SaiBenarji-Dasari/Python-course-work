from datetime import date,time,datetime,timedelta
'''
today=date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

t=time(9,35,50)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
'''
#m=datetime.now()
#print(a)
#print(a.strftime('%d-%m-%Y'))
#print(a.strftime('%d-%m-%Y %H:%M:%S'))
#print(m.strftime('%a, %d-%m-%Y %H:%M:%S'))

t=date.today()
n=datetime.now()
t7=t+ timedelta(days=7)
t3=t-timedelta(days=3)
n10=n+timedelta(minutes=10)
print(t,t7,t3)
print(n,n10)