list = [10,20,30,40]

for i in list:
    print(i, end = " ")
print()

# removing element from list
x = 10
if x in list:
    list.remove(x)

for i in list:
    print(i, end = " ")
print()
    
more_list = ['hola','suii','que_mera_bobo']



list.extend(more_list)

# another way of removing item from the list
list.pop(4) # if given idx as a parameter, it will remove that
list.pop() # othewise remove the last element from the list
for i in list:
    print(i, end = " ")