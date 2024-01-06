n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
mn = min(arr)
# print(mn, mx)
mndx = 0
mxdx = 0
for i, num in enumerate(arr):
    if num == mn:
        mndx = i
    if num == mx:
        mxdx = i
temp = arr[mndx]
arr[mndx] = arr[mxdx]
arr[mxdx] = temp

for i in arr:
    print(i, end = " ")