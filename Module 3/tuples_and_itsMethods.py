def multiple():
    return 3, 4

print(multiple())

things = "pen", "tripod", "water bottle", "charger", "phone", "web cam", "sunglass"
print(things[0])
print(things[-2])
print(things[3:6])
print(things)
print(things[::-1])

if "phone" in things:
    print("YES")

for i in things:
    print(i)

'''Tuple is immutable'''

# but if it contains mutable things, than we can change it
mega = ([1,2,3], [4,5,6])
print(mega)
print(mega[0])
mega[0][1] = 111
print(mega)