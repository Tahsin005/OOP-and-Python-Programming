'''Given a list in python and provided the index of the
elements. Write a program to swap the two elements in the list.

Example:
input: list = [23,65,19,90], idx1 = 0, idx2 = 2
output: list = [19,65,23,90]

input: list = [1,2,3,4,5], idx1 = 1, idx2 = 4
output: list = [1,5,3,4,2]'''

n = int(input())

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

 
idx1 = int(input())
idx2 = int(input())
# swapping values at index1 and index2
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)