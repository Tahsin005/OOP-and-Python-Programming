n = int(input())
f = 0
s = 1
if n == 1:
    print(0)
elif n == 2:
    print(0,1, end = " ")
else:
    print(0,1, end = " ")
    for i in range(2, n):
        tf = f
        f = s
        s = tf + s
        print(s, end = " ")