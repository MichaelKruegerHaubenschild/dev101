from random import randint

# SCHRITT 1
# Liste von simulierten Spielen erzeugen
spiele = []
ANZ_SPIELE = 100000
for a in range(1, ANZ_SPIELE):
    spiel = [False, False, False]
    spiel[randint(0,2)] = True
    spiele.append(spiel)

# SCHRITT 2
# 2 Methoden fuer die 2 Strategien
def nicht_wechseln_strategie(spiel):
    meine_wahl = randint(0,2)
    if spiel[meine_wahl] == True:
        return 1
    else:
        return 0

def wechseln_strategie(spiel):
    meine_wahl = randint(0,2)
    if spiel[meine_wahl] == False:
        return 1
    else:
        return 0

# SCHRITT 3
# Durch Spiele-Liste durchiterieren und zaehlen,
# welche Strategie wie oft gewinnt
wechseln = 0
nicht_wechseln = 0
for spiel in spiele:
    wechseln = wechseln + wechseln_strategie(spiel)
    nicht_wechseln = nicht_wechseln + nicht_wechseln_strategie(spiel)

# SCHRITT 4
# Ergebnisse ausgeben
print "Es wurden %s Spiele gespielt" % ANZ_SPIELE
print "  Wechseln Strategie Siege: " + str(wechseln)
print "  Nicht wechseln Strategie Siege: " + str(nicht_wechseln)
