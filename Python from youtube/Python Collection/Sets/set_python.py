name = {"tahsin", "tawsif", "lilin", "sharar", "abrar"}

'''cannot update elements, bu..bu..but, can remove or add elements'''

# Duplicates are not allowed

print(name)

# length of set
print(len(name))

# check type
print(type(name))

for i in name:
    print(i, end = " ")
print()

# exist or not
if "tahsin" in name:
    print("Present sir")
else:
    print("Absent sir")


# add an element 
name.add("aziz")
name.add("aziz")
# duplicate values are not allowed, so another aziz would not be there in the list
print(name)

# adding another sequence in a set
namelist = ["hello", "hi"]

name.update(namelist)

print(name)

# removing element in a set
name.remove("hi")
# name.remove("hi") 
# if a value that we want to delete is not in the set, it would show error.

# to get rid of it use
name.discard("hi") # this function will not throw error if value is not present in the set


print(name)

# joining two sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
print(s1)
print(s2)

s3 = s1.union(s2)
print(s1)
print(s2)
print(s3)
print("______________________________")
# if i want set2 to add at the end of the set1
# s1.update(s2)
print(s1)
print(s2)
print(s3)

# keep only duplicates while joining
print("______________________________")
s1.intersection_update(s2)
print(s1)
print(s3)

# keep all values except duplicates
print("______________________________")
s1.symmetric_difference_update(s2)
print(s1)
