s = input()
n = len(s)
ans = ""
cnt = 0
arr = []
for i in s:
    ans += i
    lc = ans.count('L')
    rc = ans.count('R')
    if lc == rc:
        cnt += 1
        arr.append(ans)
        ans = ""

print(cnt)
for i in arr:
    print(i)