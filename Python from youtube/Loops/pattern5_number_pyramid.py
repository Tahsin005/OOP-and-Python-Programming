# 4
#    1
#   123
#  12345
# 1234567
n = int(input())
# for i in range(1,n + 1):
#     for j in range(1, n - i + 1):
#         print(" ",end="")
#     for k in range(1, (2 * i - 1) + 1):
#         print(k,end="")
#     print() 

for i in range(1,n + 1):
    print(" " * (n - i), end = "")

    for j in range(1, 2 * i):
        print(j,end = "")
    print()