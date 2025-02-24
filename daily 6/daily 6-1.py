friend ={
    'first_name': 'Avery',
    'last_name': 'Fulmer',
    'age': 21,
    'city': 'Boston',
}

print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])

friend['favorite_number'] = 711

print(f"This person's favorite number is {friend['favorite_number']}.")

friend['city'] = 'Atlanta'

print(friend['city'])