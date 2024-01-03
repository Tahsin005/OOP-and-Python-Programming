list = [10,20,30,40]

for i in list:
    print(i, end = " ")
print()

# adding elements in the list
list.append(50) # adds the element to end of the list
list.append(60)

list.insert(4,"hola") # adds the element to the specified index

for i in list:
    print(i, end = " ")
print()
    
more_list = ['hola','suii','que_mera_bobo']

list.extend(more_list) # adds another list to the end of the list
for i in list:
    print(i, end = " ")