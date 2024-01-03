a = 0
b = 1

num = int(input())
if num == 1:
    print(a)
else:
    print(a, b, end = " ")
    for i in range(1, num - 1):
        c = a + b
        a = b
        b = c
        print(c, end = " ")