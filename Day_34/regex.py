'''
import re

pattern = r'[0-9]'
text = 'Codegnan'

res = re.match(pattern,text)

print(res.group() if res else 'Pattern is not found')

import re
pattern = r'[0-9]'
text = 'Codegnan 2026'

res = re.search(pattern,text)

print(res.group() if res else 'Pattern is not found')


import re
pattern = r'[0-9]'
text = 'Codegnan 2026'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'[0-9]'
text = 'Codegnan 2026'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())


import re
pattern = r'[0-9]{10}'
text = '1234567890'

res = re.fullmatch(pattern,text)
print(res.group() if res else 'Pattern is not found')


import re
pattern = r'[,(@]'
text = 'java,python(html@css'

res = re.split(pattern,text)
print(res)

import re
pattern = r'[0-9]'
text = 'Sai 2005'

res = re.sub(pattern,'.',text)
print(res)

import re
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect empt EkmmkmlT enlkmjlkT'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'^(91)'
text = '9121852737'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'0$'
text = '1234567890'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'to*'
text = 'to tooo too tooooooooo tdfsfd'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'to+'
text = 'to too t tooooooo tgjhkh'

res = re.findall(pattern,text)
print(res)


import re
pattern = r'91|0'
text = '91256256256250'

res = re.findall(pattern,text)
print(res)
'''
import re
pattern = r'[aeiouAEIOU]'
text = 'Sai Benarji'

res = re.findall(pattern,text)
print(res)
