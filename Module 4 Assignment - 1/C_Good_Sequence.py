n = int(input())
a = list(map(int, input().split()))
cnt = 0

mp = {}
for i in a:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1
for key, val in mp.items():
    if val < key:
        cnt += val
    elif val > key:
        cnt += val - key

print(cnt)