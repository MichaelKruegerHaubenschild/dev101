#Schreibe ein Skript, was dem Benutzer vier Additionsaufgaben stellt und
#die Antwort des Nutzers auswertet.
#Die Antwort lautet entweder richtig oder falsch, die antwort lautet

from random import randint


def ask_question():
    num1 = randint(1,100)
    num2 = randint(1,100)
    num3 = num1 + num2
    frage = "Bitte tippe die Loesung von folgender Additionsaufgabe ein: " + str(num1) + " + " + str(num2) + "  "
    ergebnis =input(frage)
    if ergebnis == num3:
        print "Richtig"
    else:
        print "Falsch, die richtige Antwort lautet " + str(num3)


ask_question()
ask_question()
ask_question()
ask_question()
