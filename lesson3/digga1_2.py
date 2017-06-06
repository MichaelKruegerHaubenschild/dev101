number1 = raw_input("Bitte geben Sie ein Zahl ein! ")
number2 = raw_input("Bitte geben Sie noch eine Zahl ein!!! ")
number3 = input("Gib jetzt 1 ein, um zu multiplizieren, oder 2 um zu dividieren ")
if number3 == 1:
    print (number1*number2)
elif number3 == 2:
    print float(float(number1)/float(number2))
else:
    print " ERROR : PLEASE CONTACT SUPPORT AT EUROPACE "
