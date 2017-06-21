Liste =[]

def list_info(wert):
    Liste.append(wert)

while True: ## ist eine Endlosschleife
	try:
		wert = raw_input ("Bitte gib die Werte der Liste ein. 0 fuer Exit.  ")
		wert = int(wert)
		if wert !=0:
			print ("Danke!")
			list_info(wert)
			continue
		else:
			print("Anzahl der Werte in Liste: "+str(len(Liste)))
			print("Das erste Element ist: ")+str(Liste[0])
			print("Das letzte Element ist: ")+str(Liste[-1])
			break
	except ValueError:
		print("Bitte gib eine natuerliche Zahl ein.")
