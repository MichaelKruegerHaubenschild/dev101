
number1 = raw_input("Bitte nennen Sie eine Zahl ")
number2 = raw_input("Bitte nennen Sie eine weitere Zahl ")
if int(number1) > int(number2):
    print "Die hoechste Zahl ist " + str(number1)
elif int(number1) == int(number2):
    print "Die Zahlen sind gleich gross"
else:
    print "Die hoechste Zahl ist " + str(number2)
