from random import randint

# SCHRITT 1
# Liste von simulierten Spielen erzeugen
spiele = []

ANZ_SPIELE = 1000

for a in range(1, ANZ_SPIELE):
    counter = 0
    wurf = [1, 2, 3, 4, 5, 6]
    for e in wurf:
        wurf[counter] = randint (1,6) #randint[1,6]
        counter = counter + 1

    spiele.append(wurf)

#print spiele

# SCHRITT 2
#2 Methoden
def list_Vergleich(spiel, Ergebnis):
    #print spiel
    #spiel = [1,6,6,6,6,6]
    meine_wahl = Ergebnis
    spiel.sort()
    value = cmp(spiel, meine_wahl)
    #print value
    if value == 0:
        return 1

    else:
        return 0

def ungerade_Zahlen(spiel):

    num = 0
    for e in spiel:
        if e % 2:
            num = num + 1
    #print num
    if num == 6:
        #print spiel
        return 1
    else:
        return 0


# # SCHRITT 3
# # Durch Spiele-Liste durchiterieren und zaehlen,
# # wie oft die Wurfe erscheinen
sechser = 0
alle_Zahlen = 0
ungerade = 0
Ergebnis1 =  [6,6,6,6,6,6]
Ergebnis2 =  [1,2,3,4,5,6]

for spiel in spiele:
    #print alle_sechs(spiel)
    sechser = sechser + list_Vergleich(spiel, Ergebnis1)
    alle_Zahlen = alle_Zahlen + list_Vergleich(spiel, Ergebnis2)
    ungerade = ungerade + ungerade_Zahlen(spiel)
#    nicht_wechseln = nicht_wechseln + nicht_wechseln_strategie(spiel)

# # SCHRITT 4
# # Ergebnisse ausgeben
print "Es wurden %s Spiele gespielt" % ANZ_SPIELE
print "  Alle Sechs kamen vor: " + str(sechser)
print "  Alle Zahlen kamen genau einmal vor: " + str(alle_Zahlen)
print "  Nur ungerade Zahlen kamen vor: " + str(ungerade)
