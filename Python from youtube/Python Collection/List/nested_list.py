fruits = ["apple", "mango", "cherry", "banana"]
fruits.insert(2,["kiwi", "papaya"])
print(fruits)
print()
print(fruits[2][0], fruits[2][1])
fruits.insert(2,[1,2,3,4,5,6,7])
print(fruits)
print(fruits[2])

for _ in fruits[2]:
    print(_) 