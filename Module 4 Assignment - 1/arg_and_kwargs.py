def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))

def function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function(name = 'Tahsin', age = 21, city = 'Cox\'s Bazar')
