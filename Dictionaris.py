mycat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(mycat['size'])

print('My cat has' + mycat['color'] + 'fur')

spam = {12345: 'Luggage Combination', 42: 'The answer'}

val = [1, 2, 3] == [3,2,1]

eggs = {'name':'Zophie','Species':'cat','age':8}

ham = {'Species':'cat','name':'Zophie','age':8}

print(eggs == ham)

'name' in eggs # Chequear si existe la palabra key

list(eggs.keys()) #Claves de cada campo
list(eggs.values()) # Valores de cada campo
list(eggs.items()) #Toda la informacion

for k,v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

eggs.get('age', 0)

picniItems = {'apples': 5, 'cups' : 2}
print('I am bringing' + str(picniItems.get('napkins', 0)) + 'to the picnic')

if 'color' not in eggs:
    eggs['color'] = 'black'

eggs = {'name':'Zophie','Species':'cat','age':8}
eggs.setdefault('color', 'black')

eggs = {'name':'Zophie','Species':'cat','age':8}
eggs.setdefault('color', 'orange')


###################################################################

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)