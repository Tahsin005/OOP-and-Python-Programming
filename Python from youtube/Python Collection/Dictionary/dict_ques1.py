'''Given a dictionary in python, Write a program to find the sum of ll items in the dictionary
input: {'a': 100, 'b': 200, 'c': 300}
output: 600

input: {'x': 25, 'y': 18, 'z': 45}
output: 88

'''
input = {'a': 100, 'b': 200, 'c': 300}
# input = {'x': 25, 'y': 18, 'z': 45}
output = 0

# for x,y in input.items():
#     output += y
# print(output)

# another easy way
print("The sum of dict values is :", sum(input.values()))