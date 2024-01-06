n, q = map(int, input().split())

arr = list(map(int, input().split()))
pre = [0] * n
pre[0] = arr[0]
for i in range(1, n):
    pre[i] = arr[i] + pre[i - 1]

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == 0:
        total = pre[r] - 0
    else:
        total = pre[r] - pre[l - 1]
    print(total)