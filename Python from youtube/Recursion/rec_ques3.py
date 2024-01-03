'''Make a function which calculates 'a' raised to 
the power 'b' using recursion'''
def aRaisedTob(a,b):
    if b == 0:
        return 1
    return a * aRaisedTob(a,b - 1)

print(aRaisedTob(2,5))