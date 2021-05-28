############################################
boundary = 3
'''if boundary == 2:
    x = 1
else:
    x = 0
'''
x = 1 if boundary == 2 else 0
print(x)

############################################

num1 = 10_000_000  # underscore doesn't effect the code in int
print(f'{num1:,}')

############################################
'''
file = open('test.txt', 'r')
file_contents = file.read()
file.close()
'''
with open('test.txt', 'r') as file:
    file_content = file.read()

print(len(file_content.split()))

############################################

names = ['ram', 'syam', 'hari', 'madan']

'''index = 1
for name in names:
    print(index, name)
    index += 1
'''

for index, name in enumerate(names, start=1):
    print(index, name)

############################################

names = ['Peter', 'Bruce', 'Clark', 'Tony']
heroes = ['Spiderman', 'Batman', 'Superman', 'Ironman']

"""
for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}")
"""
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")

######################################################

# unpacking variables

a, _, *c, d = (1, 2, 3, 4, 5)  # use _ to ignore the variable while unpacking
print(a)  # a = 1
print(c)  # c = [2, 3]
print(d)  # d = 5


#####################################################

class Person:
    pass


first_key = 'first'
first_val = 'Corey'

person1 = Person()

'''
person1.first = 'Corey'
'''

setattr(Person, first_key, first_val)
print(person1.first)

value = getattr(Person, first_key)
print(value)

# example
person_info = {'first': 'Judy', 'last': 'Rod'}

person2 = Person()
for key, value in person_info.items():
    setattr(person2, key, value)

for key in person_info:
    value = getattr(person2, key)
    print(value)

####################################################
