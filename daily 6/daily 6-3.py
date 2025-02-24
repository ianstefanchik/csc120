people = []

friend ={
    'first_name': 'Avery',
    'last_name': 'Fulmer',
    'age': 21,
    'city': 'Boston',
}

people.append(friend)

friend ={
    'first_name': 'Duncan',
    'last_name': 'Ferguson',
    'age': 22,
    'city': 'Dahlonega',
}

people.append(friend)

friend ={
    'first_name': 'Simon',
    'last_name': 'Domencic',
    'age': 20,
    'city': 'Millersville',
}

people.append(friend)

for friend in people:
    print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])