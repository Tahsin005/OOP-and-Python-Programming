# function is a first class object

def double_decker():
    print('Starting a double decker')
    def inner_fun():
        print('Inside the inner')
        return 'suii '
    return inner_fun

# print(double_decker())
# print(double_decker()())


def do_something(work):
    print('Work started')
    # print(work)
    work()
    print('Work ended')

# do_something(2)
# do_something('Suuiiiiii')

def coding():
    print('Coding in python')
    
do_something(coding)