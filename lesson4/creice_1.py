def gib_max (wert1,wert2,wert3):
  ergebnis = max (wert1,wert2,wert3)
  return ergebnis

number1 = int(raw_input ("Bitte gib eine Zahl ein: "))
number2 = int(raw_input ("Bitte gib eine andere Zahl ein: "))
number3 = int(raw_input ("Bitte gib eine dritte Zahl ein: "))

ergebnis = gib_max(number1,number2,number3)
print ergebnis 