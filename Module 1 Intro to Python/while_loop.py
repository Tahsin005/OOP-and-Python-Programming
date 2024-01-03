# num = 1

# while num <= 10:
#     print(num)
#     num += 1

# while num <= 10:
#     if num == 5:
#         break
#     print(num)
#     num += 1
num = 1
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
    