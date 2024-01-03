fruits = ["apple", "banana", "jackfruit", "watermelon"]
for i in fruits:
    print(i, end=" ")


mix = [1,2,"banana","yellow",9.99]
print()
for i in mix:
    print(i, end = " ")
print()
length = len(mix)
for i in range(length):
    print(mix[i], end = " ")


print()
list = [10,20,30,40]
# indexing in a list
print(list[1])
print(list[-3])

# print(list[1:3])
temp = list[1:3]
print(temp)

temp = list[-3:-1]
# print(list[-3:-1])
print(temp)

length_of_list = len(list)
# print(length_of_list)

for i in range(length_of_list - 1, -1, -1):
    print(list[i], end = " ")

for i in reversed(range(length_of_list)):
    print(list[i], end = " ")