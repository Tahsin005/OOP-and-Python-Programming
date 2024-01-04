n = int(input())
# array = list(map(int, input().split()))
array = input().split()
for i in range(0,n):
    array[i] = int(array[i])


for i in range(n - 1, -1, -1):
    print(array[i], end = " ")