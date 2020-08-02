def fact(n):
    if n == 0:
        return 1
    else:                                               #Recursive method
        return n * fact(n - 1)
    

x = fact(10)
print(x)


def factorial(n):
    count = n - 1
    while count > 1:
        n *= count                                      #Non-recursive method
        count -= 1
    return n


#print(factorial(10))
