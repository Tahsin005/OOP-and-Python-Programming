n = int(input())
arr = list(map(int, input().split()))

rev = arr[::-1]
flag = True
for i in range(n):
    if(arr[i] != rev[i]):
        flag = False
        break
if flag == True:
    print("YES")
else:
    print("NO")