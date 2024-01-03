# A simple function to sum two numbers
def add(n1 = 0,n2 = 0):
    print("n1:", n1)
    print("n2:", n2)
    sum = n1 + n2
    return sum

# positional argument
print("The sum is :", add(2,93))

# keyword argument (named argument)
print("The sum is :", add(n1=3, n2= 5))
    # Here the sequence doesnot matter
print("The sum is (not in original sequence) :", add(n2=99, n1=1))

# default arguments
print("The sum is :", add())

'''arbitary arguments'''
# the argument will be taken as a tuple
def add_all_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


output = add_all_numbers(1,2,3,4,5)
print("The sum of add_all_numbers :", output)

# arbitary argment but will be dictionary
def student_info(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)

student_info(name = "tahsin", age = 22, city = "cox's bazar")
student_info(name = "messi", age = 37, city = "rosario")