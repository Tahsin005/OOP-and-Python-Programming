import math
def timer(func):
    def inner(*args, **kwargs):
        print('timer started')
        # print(func)
        func(*args, **kwargs)
        print('timer ended')
    return inner

# timer()()
@timer # When we use a function as a decorator, we need to consider all of its parameter
def get_factorial(n):
    print('getting factorial')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}')

get_factorial(5)

# bhejailla way to decorate
# timer(get_factorial)()