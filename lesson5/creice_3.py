## Alle Eintraege groesser 10 rausschmeissen

Liste =[]

def list_info(wert):
    Liste.append(wert)

def less_ten(Liste):
	elemente = len(Liste)
	print ("Elemente"+str(elemente))
	i=0
	while i < elemente:
		print "Zaehler For Schleife "+str(i)+" wird durchlaufen"
		print "Altes Listenlement " +str(Liste[i])
		if Liste[i]>10 :
			print "Element "+str(Liste [i])+" wird geloescht"
			del Liste[i]
			print "Selbe Position pruefen! " # Es muss noch ein Mal die selbe Position geprüft werden!
			elemente = elemente-1 # Die Liste ist kürzer geworden!
		else:
			i=i+1
	return Liste
## Warum darf ch nicht new_list = Liste sagen?

while True: ## ist eine Endlosschleife
	try:
		wert = raw_input ("Bitte gib die Werte der Liste ein. 0 fuer Exit.  ")
		wert = int(wert)
		if wert !=0:
			print ("Danke!")
			list_info(wert)
			continue
		else:
			print("Deine alte Liste:  "+str(Liste))
			less_ten(Liste)
			print("Deine neue Liste:  "+str(Liste))
			break
	except ValueError:
		print("Bitte gib eine natuerliche Zahl ein.")
