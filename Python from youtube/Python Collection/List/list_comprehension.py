'''When we want to make a new list of items 
from an existing list'''

'''Long way'''
list = [40,20,30,10]
fruits = ["apple", "mango", "cherry", "banana"]
new_list = []
for i in list:
    if i > 25:
        new_list.append(i)

for i in new_list:
    print(i, end = " ")
print()


'''Using list comprehension way'''

final_list = [i for i in list if i > 25]
print(final_list)

print(fruits)
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

final_fruits = new_fruits.copy()
print(final_fruits)

# list concatinate using '+'
new_fruits += fruits
print(new_fruits)