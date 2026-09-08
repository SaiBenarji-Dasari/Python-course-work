'''
import re
fullname = input('Enter your full name: ')
pattern= r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.fullmatch(pattern,fullname)
print("Valid name" if res else "Invalid name")

import re
email = input('Enter your email: ')
pattern= r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res = re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")

import re
phone_number = input('Enter your phone number: ')
pattern= r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern,phone_number)
print("Valid phone number" if res else "Invalid phone number")

import re
password = input('Enter your password: ')
pattern= r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,25}$'
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")

import re
username = input('Enter your username: ')
pattern= r'^[A-Za-z_0-9]{2,}'
res = re.fullmatch(pattern,username)
print("Valid username" if res else "Invalid username")

import re
aadhar = input('Enter your aadhar number: ')
pattern= r'^\d{12}$'
res = re.fullmatch(pattern,aadhar)
print("Valid aadhar number" if res else "Invalid aadhar number")
'''
import re
pancard = input('Enter your pancard number: ')
pattern= r'^[A-Z]{5}\d{4}[A-Z]{1}$'
res = re.fullmatch(pattern,pancard)
print("Valid pancard number" if res else "Invalid pancard number")