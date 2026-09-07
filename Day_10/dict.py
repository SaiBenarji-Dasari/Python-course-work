Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data ={"name":"jagadeesh","batch":64,"course":"PFS"}
data
{'name': 'jagadeesh', 'batch': 64, 'course': 'PFS'}
data[name]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[name]
NameError: name 'name' is not defined
data["name"]
'jagadeesh'
data["batch"]
64
64 in data
False
data.get("age","key is not present")
'key is not present'
data.get("course","key is not present")
'PFS'
data["batch"]=789
data
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS'}
data["skills"]=["Python","sql","flask"]
data
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask']}
data.pop[age]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data.pop[age]
NameError: name 'age' is not defined
data["age']=23
     
SyntaxError: unterminated string literal (detected at line 1)
data["age"]=21
     
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21}
data.update({"phone":7893952075,"email":"jagadeesh.vinnakota@gmail.com","surname":"vinnakota"})
     
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.pop("age")
     
21
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.pop("phone")
     
7893952075
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.popitem("surname")
     
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data.popitem("surname")
TypeError: dict.popitem() takes no arguments (1 given)
del data['name']
     
data
     
{'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.popitem()
     
('surname', 'vinnakota')
data
     
{'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'email': 'jagadeesh.vinnakota@gmail.com'}
data.popitem()
     
('email', 'jagadeesh.vinnakota@gmail.com')
data.popitem()

('skills', ['Python', 'sql', 'flask'])
data
     
{'batch': 789, 'course': 'PFS'}
data.popitem()

('course', 'PFS')
data
     
{'batch': 789}
data.popitem()

('batch', 789)
data
     
{}
data.clear()
     
data
     
{}
data
     
{}
data={'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
     
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.keys()
     
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phone', 'email', 'surname'])
data.values()
     
dict_values(['jagadeesh', 789, 'PFS', ['Python', 'sql', 'flask'], 21, 7893952075, 'jagadeesh.vinnakota@gmail.com', 'vinnakota'])
data,items()
     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    data,items()
NameError: name 'items' is not defined. Did you mean: 'iter'?
data.items()
     
dict_items([('name', 'jagadeesh'), ('batch', 789), ('course', 'PFS'), ('skills', ['Python', 'sql', 'flask']), ('age', 21), ('phone', 7893952075), ('email', 'jagadeesh.vinnakota@gmail.com'), ('surname', 'vinnakota')])
sorted.data()
     
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    sorted.data()
AttributeError: 'builtin_function_or_method' object has no attribute 'data'
sorted(data)
     
['age', 'batch', 'course', 'email', 'name', 'phone', 'skills', 'surname']
sorted(data,reverse=True)
     
['surname', 'skills', 'phone', 'name', 'email', 'course', 'batch', 'age']
max(data)
     
'surname'
min(data)
     
'age'
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
dat["age"]
     
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dat["age"]
NameError: name 'dat' is not defined. Did you mean: 'data'?
data["age"]
     
21
data.get("age")
     
21
data.setdefault("age",0)
     
21
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
data.setdefault("name",'')
     
'jagadeesh'
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
len(data)
     
8
data
     
{'name': 'jagadeesh', 'batch': 789, 'course': 'PFS', 'skills': ['Python', 'sql', 'flask'], 'age': 21, 'phone': 7893952075, 'email': 'jagadeesh.vinnakota@gmail.com', 'surname': 'vinnakota'}
>>> a={1:4,2:5,3:9}
...      
>>> b=a
...      
>>> b
...      
{1: 4, 2: 5, 3: 9}
>>> a
...      
{1: 4, 2: 5, 3: 9}
>>> c=a.copy()
...      
>>> c
...      
{1: 4, 2: 5, 3: 9}
>>> c.add(4:6)
...      
SyntaxError: invalid syntax
>>> c.add[4:6]
...      
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    c.add[4:6]
AttributeError: 'dict' object has no attribute 'add'
>>> c[4]=4
...      
>>> c
...      
{1: 4, 2: 5, 3: 9, 4: 4}
>>> a
...      
{1: 4, 2: 5, 3: 9}
>>> b
...      
{1: 4, 2: 5, 3: 9}
>>> c
...      
{1: 4, 2: 5, 3: 9, 4: 4}
>>> d= dict.fromkeys(["a","b"],0)
...      
>>> d
...      
{'a': 0, 'b': 0}
