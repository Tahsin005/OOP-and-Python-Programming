person = {'name' : 'kala pakhi', 'address' : 'kaliapur', 'age' : 23, 'job' : 'student'}
print(person)
print(person['address'])
print(person.keys())
print(person.values())

person['language'] = 'python'
print(person)
person['name'] = 'sada pakhi'
del person['age']
print(person)

for k, v in person.items():
    print(k, v)