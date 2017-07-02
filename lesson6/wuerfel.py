from random import randint

nursechsen = 0
nurungerade = 0
allezahlen = 0

wuerfe = []
ANZ_WUERFE = 100000
for a in range(0,ANZ_WUERFE):
    einzelnerwurf = []
    for a in range(1,7):
        wuerfel = randint(1,6)
        einzelnerwurf.append(wuerfel)
    wuerfe.append(einzelnerwurf)

    if einzelnerwurf == [6,6,6,6,6,6]:
        nursechsen = nursechsen + 1
    elif:
        counter = 0
        for e in einzelnerwurf:
            if e% 2 == 1:
                counter = counter + 1
            if counter == 6:
                nurungerade = nurungerade + 1
    else:
        sortiert = sorted(einzelnerwurf)
        if sortiert == [1,2,3,4,5,6]:
            allezahlen = allezahlen + 1

print nursechsen
print nurungerade
print allezahlen
