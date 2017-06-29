from random import randint, choice


liste = [1,2,3]
listezwei = [1,2,3]
gewinn = randint(1,3)
liste.remove(gewinn)
listezwei.remove(gewinn)
print liste

wahleins = input("Bitte gebe eine Zahl von 1,3 ein ")
if wahleins in liste:
    listezwei.remove(wahleins)
    print str(listezwei) + " ist eine falsche Wahl"
else:
    loeschen = randint(0,1)
    liste.remove(list[loeschen])
    print list[0]

frage2 = input("Welche Tuer waehlst du, nachdem das Programm eine Tuer geoeffnet hat? ")
if  input == wahleins:
    print "Diese Tuer habe ich schon geoeffnet"
elif frage2 in liste:
    print "Verloren"
else:
    print "Gewonnen"
