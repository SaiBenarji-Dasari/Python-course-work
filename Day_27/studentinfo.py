import json
'''with open('data.json','r') as file:
    data=json.load(file)
data["name"]="Sai Benarji"
data["branch"]="CSE"

with open('data.json','w') as file:
    print(data,file,'indent=4')
'''
student={
    "name":"Benarji",
    "age": 21,
    "Course":"PFS"
}    
json_data=json.dumps(student)
print(json_data)

student=json.loads(json_data)
print(student)
print(type(student))