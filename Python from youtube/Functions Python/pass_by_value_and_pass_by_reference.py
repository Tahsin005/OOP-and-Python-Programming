# pass by value (immutable objects: strings, integers, float, tuples)

def addOne(x):
    x += 1
    print("Inside function :", x)

x = 5
addOne(x)
print("Outside function :", x)


# pass by reference (mutable objects: lst, dictionary) 
# - changes inside the function will effect original object

def modifyList(lst):
    lst.append(7)
    # lst = [6,4,0]
    '''if we try to modify the list using 
    assignment operator, the list wont change
    outside the function, as it would create
    another copy of its own list which is
    different from the original list outside 
    the function'''
    print("Inside function :", lst)

lst = [1,2,3,4]
modifyList(lst)
print(lst)

# 7, 47