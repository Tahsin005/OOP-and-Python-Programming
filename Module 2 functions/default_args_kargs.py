def sum(n1, n2, n3 = 0):
    res = n1 + n2 + n3
    return res
# total = sum(99,11,5)
# print(total)

# args
def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum


total = all_sum(1,2,3,4)
print("All sum :", total)