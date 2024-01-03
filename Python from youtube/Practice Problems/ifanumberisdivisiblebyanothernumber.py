# Solution 1 using for loop
print("The number divisible by 13 are: ")
for i in range(1,100):
    if i % 13 == 0:
        print(i)

# Solution 2 using lambda function and filter()
'''Lambda function is an anonymus function. It is a temporary function we use 
when we dont need to use perment function.             
And filter function filters the output and prints it if it satisfies the given condition'''

l = [39, 48, 26, 98, 33, 67, 87]

result = list(filter(lambda x: x % 13 == 0, l))
print(result)