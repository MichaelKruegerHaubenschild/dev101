print "Bitte gebe zwei Zahlen ein"
zahl1 = input()
zahl2 = input()
if zahl1 > zahl2:
    print "Die groessere Zahl lautet " + str(zahl1)
else:
    print "Die groessere Zahl lautet " + str(zahl2)
operation = input("Jetzt wird die dividiert oder multipliziert. Gebe 1 ein, um beide Zahlen zu multiplizieren. Gebe 2 ein um die erste Zahl durch die zweite zu dividieren")
if operation == 1:
    multip = zahl1 * zahl2
    print "Das Ergebnis lautet " + str(multip)
else:
    div = zahl1 / zahl2
    print "Das Ergebnis lautet " + str(div)
