# Hier wird ein neues Modul "importiert". Das erlaubt es, die randint() Funktion
# in diesem Skript zu verwenden
from random import randint

# 2 random Ints zwischen 1 und 100 erzeugen

def ask_question():
    # Diese Funktion musst du erweitern
    num1 = randint(1,100)
    num2 = randint(1,100)
    print "Was ist " +str(num1)+ " + " +str(num2)+ "?"
    user_ergebnis = int(raw_input ("Bitte gib Dein Ergebnis ein: "))
    richtiges_ergebnis = num1 + num2
    if user_ergebnis == richtiges_ergebnis:
        print "Du hast korrekt gerechnet!"
    else:
        print "Falsch! Das richtige Ergebnis waere "+str(richtiges_ergebnis)

# Die Funktion wird 4 mal aufgerufen. Ab hier nichts mehr aendern.
ask_question()
ask_question()
ask_question()
ask_question()
