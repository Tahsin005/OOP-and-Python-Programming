numbers = [12,66,98,6,12,78,98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(33)
print(numbers_set)
numbers_set.remove(12)
print(numbers_set)

if 9 in numbers_set:
    print("9 exists")
if 98 in numbers_set:
    print("98 exists")

a = {1, 3, 5}
b = {1, 3, 5, 4, 2}
print(a & b)
print(a | b)
res = a.union(b)
res = a.intersection(b)
res = b.issubset(a) # if b is a subset of a or not
print(res)