a, b = input().split()
x = int(a)
y = int(b)
sum = 0
for i in range(2, y + 1, 2):
    sum += (x ** i)
print(sum)