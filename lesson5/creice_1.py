# Funktionen
def ansprache(Name,truth):
    if truth is True:
        return "You are the best "+str(Name)
    elif truth is False:
        return str(Name)+", you suck!"

Name = raw_input ("Bitte gib Deinen Namen ein: ")
truth = int(raw_input("Bitte gib 0 fuer falsch und 1 fuer wahr ein: "))
truth = bool (truth)
print truth
reply = ansprache(Name,truth)
print reply
