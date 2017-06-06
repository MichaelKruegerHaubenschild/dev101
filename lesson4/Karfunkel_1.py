

def my_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print my_max(2,3,4)
print my_max(5,6,7)
print my_max(8,9,10000000)
