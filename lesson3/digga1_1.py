
number1 = raw_input("Bitte nennen Sie eine Zahl ")
number2 = raw_input("Bitte nennen Sie eine weitere Zahl ")
if number1 > number2:
    print "Die hoechste Zahl ist " + str(number1)
elif number1 == number2:
    print "Die Zahlen sind gleich gross"
else:
    print "Die hoechste Zahl ist " + str(number2)
