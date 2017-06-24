# Dieses Script loest das "Der Preis ist heiss Problem"
# Aufgabe: Es gibt drei Tore. Hinter einem Tor liegt der Hauptgewinn.
# Der Kandidat entscheidet sich fuer ein Tor. Der Moderator oeffnet daraufhin ein anderes Tor, hinter dem der Zonk liegt.
# Soll der Kandidat nun seine Meinung aendern, oder bei seiner urspruenglichen Wahl bleiben? Wie sind die Wahrscheindlichkeiten?

#Global gueltige Variablen definieren
x = 0
neues_Tor = 0
gewonnen = 0
verloren = 0
quote = 0.00

def Kandidat_wechselt (kandidat_wahl_tor,moderator_tor):
    global neues_Tor
    for x in range (1,4):
        if x == moderator_tor:
            continue
        if x == kandidat_wahl_tor:
            continue
        else:
            neues_Tor = x
            return neues_Tor
            break


from random import randint
anzahl_versuche = int(raw_input ("Wie viele Versuche soll ich simulieren?: "))

for I in range(anzahl_versuche):
    hauptgewinn = randint(1,3)
    #print "Hauptgewinn ist hinter Tor:  " +str(hauptgewinn)
    kandidat_wahl_tor = randint(1,3)
    #print "Kandidat waehlt Tor:  "+str(kandidat_wahl_tor)
    # Moderator oeffnet Tor
    while True: ## ist eine Endlosschleife
        moderator_tor = randint(1,3)
        if moderator_tor == hauptgewinn or moderator_tor ==kandidat_wahl_tor:
           continue
        else:
           break
    #print "Moderator oeffnet Tor:  "+str(moderator_tor)
    # Kandidat entscheidet sich zum Wechsel des Tores
    Kandidat_wechselt(kandidat_wahl_tor,moderator_tor)
    #print "Neues Tor Kandidatenwahl:  "+str(neues_Tor)
    if neues_Tor == hauptgewinn:
        gewonnen = gewonnen + 1
    else:
        verloren = verloren + 1

print "Ergebnis: "
print "Anzahl Versuche: "+str(anzahl_versuche)
print "Anzahl Gewinne: "+str(gewonnen)
print "Anzahl Verloren: "+str(verloren)
