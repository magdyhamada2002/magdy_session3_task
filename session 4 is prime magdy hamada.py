x = 13
i = int(x ** 0.5)
print(i)
def is_prim(x):
    z = 0
    if x<=1:
        return False
    elif x==2:
        return True
    if x>2:
        for lop in range(2,i+1):
            if ( x % lop == 0):
                z = 1
                break
        if z == 0:
            return True
        else:
            return False
    else:
        return False
print(is_prim(x))