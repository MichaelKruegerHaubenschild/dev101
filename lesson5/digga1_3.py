def less_than_10(Numlist):
    NewList = []

    for n in Numlist:
        
        if n < 10:
            NewList.append(n)

    return NewList


list = [1,3,5,11,22,1,1,100,3]

print less_than_10(list)
