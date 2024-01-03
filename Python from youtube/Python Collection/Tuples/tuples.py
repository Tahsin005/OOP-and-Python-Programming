''' Creating tuple of size one'''
fruits = ("apple",)
fruit = tuple(("apple"))
print(type(fruits), type(fruit))
'''if we create a tuple of size one, we have to use a comma(,) too. Otherwise program wouldnot be able to distinguish between tuple and normal things cause we use () for many other things in the code'''

colors = ("blue", "green", "red")
mix = ("red", "blue", 1,5, 0.3,"green", True, "red")
for _ in mix:
    print(_, end = " ")
print()

# type of tuple
print(type(mix))


# length of tuple 
print(len(mix))


# accessing items in tuple

# normal indexing
print(mix[4])

# negative indexing
print(mix[-2])

# range indexing
print(mix[0:]) # if we dont specify the ending point, it will go from the starting point to the last of the tuple / list 
print(mix[0:5])

# check if an item exist or not
if "green" in mix:
    print("Present")
else:
    print("Not present")

print("------------------------------------")
# traverse in tuple
for i in mix:
    print(i, end = " ")
print()

print("------------------------------------")
# concatenate two tuples
mix += colors
print(mix)

# unpacking in tuple
print("------------------------------------")
mix1, mix2, mix3, mix4, mix5, mix6, mix7, mix8, mix9, mix10, mix11 = mix
print(mix1, mix2, mix3, mix4, mix5, mix6, mix7, mix8, mix9, mix10, mix11)

print("------------------------------------")
colors1, colors2, colors3 = colors
print(colors1, colors2, colors3)

#5,44,33
#tuple vs list

