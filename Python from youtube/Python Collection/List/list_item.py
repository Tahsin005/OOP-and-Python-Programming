fruits = ["apple", "banana", "jackfruit", "watermelon"]
for i in fruits:
    print(i, end=" ")


mix = [1,2,"banana","yellow",9.99]
print()
for i in mix:
    print(i, end = " ")

# We can also print list like this.
print(fruits, mix)
print(type(fruits),type(mix))

# Length of the list:
print(len(mix),len(fruits))

# Check if an item is present in the list:
print("banana" in fruits)

if "banana" in fruits:
    print("Banana is part of the list. ")
if "kiwi" not in fruits:
    print('Kiwi is not part of the fruits')