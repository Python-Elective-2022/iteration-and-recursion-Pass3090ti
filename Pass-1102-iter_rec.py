# Collaborate with Leo

def iterativePower(base, exp): 
    '''
    Iterative power:     
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        base1 = base
        for i in range (exp - 1):
            base *= base1 
        return base

print(iterativePower(2,3))



def recursivePower(base, exp):
    '''
    Recursive power:
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(2,3))