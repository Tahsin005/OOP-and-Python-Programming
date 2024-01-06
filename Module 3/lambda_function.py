# def doubled(x):
#     return x * 2

doubled = lambda num : num * 2
squared = lambda num : num ** 2

res = doubled(44)
sq = squared(9)
# print(res, sq)

add = lambda x,y : x + y
sum = add(11,33)
# print(sum)

numbers = [12,66,98,6,12,78,98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x : x * 2, numbers)
# print(list(doubled_nums))

actors = [
    {'name' : 'shabana', 'age' : 65},
    {'name' : 'shabnoor', 'age' : 45},
    {'name' : 'sabila noor', 'age' : 30},
    {'name' : 'srabonti', 'age' : 38},
    {'name' : 'shaon', 'age' : 47}
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
fivers = filter(lambda actor: actor['age'] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))

num = lambda a:a*a
print(num(2**2))

name = actors.keys()
print(name)