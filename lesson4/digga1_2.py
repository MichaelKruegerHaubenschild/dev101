# Hier wird ein neues Modul "importiert". Das erlaubt es, die randint() Funktion
# in diesem Skript zu verwenden
from random import randint

# 2 random Ints zwischen 1 und 100 erzeugen
num1 = randint(1,100)
num2 = randint(1,100)
#print "Ich habe 2 random Ints ausgewaehlt: " + str(num1) + " und " + str(2)

def ask_question():
    # Diese Funktion musst du erweitern
    num1 = randint(1,100)
    num2 = randint(1,100)
    Ergebnis = num1 + num2
    print "Ergebnis: " + str(Ergebnis)
#print str(Ergebnis)
    Answer = input("Was ist das Ergebnis von :"  + str(num1) +  " plus " + str(num2))

    if int(Answer) == int(Ergebnis):
        print "correct"
    else:
        print "false"



# Die Funktion wird 4 mal aufgerufen. Ab hier nichts mehr aendern.
ask_question()
ask_question()
ask_question()
ask_question()
