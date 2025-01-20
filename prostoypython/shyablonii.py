import re

source = '''i wish i may,  i wish i might
have a dish of fish tonight.'''

print(re.findall('wish', source))

print(re.findall('wish|fish', source))

print(re.findall('^wish', source))

print(re.findall('^i wish', source))

print(re.findall('fish$', source))

print(re.findall('fish tonight.$', source))

print(re.findall('fish tonight\.$', source))

print(re.findall('[wf]ish', source))

print(re.findall('[wsh]+', source))

print(re.findall('ght\W', source))

print(re.findall('i (?=wish)', source))

print(re.findall('(?<=i) wish', source))

print(re.findall('\bfish', source))
print(re.findall(r'\bfish', source))



m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group("DISH"))
print(m.group("FISH"))
