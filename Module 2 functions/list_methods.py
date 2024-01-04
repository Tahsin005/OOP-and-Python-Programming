numbers = [12, 45, 98, 68]
numbers.append(56)

numbers.insert(2, 88)

messi = [1,2,3,4,5]
numbers.extend(messi)
numbers.extend(messi)

if 5 in numbers: # otherwise will throw an error
    numbers.remove(5)
print(numbers)


last = numbers.pop()
print(numbers, last)

idx = numbers.index(56)
print(idx)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

cnt3 = numbers.count(3)
print("Count of 3 is :", cnt3)