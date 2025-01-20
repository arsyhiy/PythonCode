from collections import Counter
x= 'кукарача'
counter = Counter(x)
print(counter['а'])

print('Mary had a little lamb'.count('a'))


import re
my_string = "Mary had a little lamb"
print(len(re.findall("a", my_string)))


from collections import Counter
my_str = "Mary had a little lamb"
counter = Counter(my_str)
print(counter['a'])


from collections import defaultdict

text = 'Mary had a little lamb'
chars = defaultdict(int)

for char in text:
    chars[char] += 1
    
print(chars['a'])
print(chars['t'])
print(chars['w']) # element not present in the string, hence print 0


from collections import defaultdict

text = 'Mary had a little lamb'
chars = defaultdict(int)

for char in text:
    chars[char] += 1
    
print(chars['a'])
print(chars['t'])
print(chars['w']) # element not present in the string, hence print 0

sentence = ['M', 'ar', 'y', 'had', 'a', 'little', 'l', 'am', 'b']
print(sum(map(lambda x : 1 if 'a' in x else 0, sentence)))


sentence = 'Mary had a little lamb'    
count = 0
for i in sentence:
    if i == "a":
        count = count + 1
print(count)


my_string = "Mary had a little lamb"
print(sum(char == 'a' for char in my_string))
