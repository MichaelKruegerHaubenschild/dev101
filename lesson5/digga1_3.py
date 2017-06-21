def less_than_10(Numlist):
    NewList = []

    for n in Numlist:

        if n < 10:
            NewList.append(n)

    return NewList



def less_than_10_V2(Numlist):

    for n in reversed(Numlist):

        if n > 10:
            Numlist.remove(n)

    return Numlist


list = [1,3,5,11,22,1,1,100,111,222,13,4,5,11111,1]

print less_than_10_V2(list)
