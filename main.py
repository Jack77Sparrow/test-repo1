
def factorial(x):
    '''
    something
    '''
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))