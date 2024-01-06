s = input().split()
n = len(s)
l = list(s)
for i in range(n):
    val = l[i]
    if i == n - 1:
        print(val[::-1])
    else:
        print(val[::-1], end = " ")
        