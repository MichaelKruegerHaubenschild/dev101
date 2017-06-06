## Homework lesson 3 / 1
## Autor: Christian Driesen
##

while True: ## ist eine Endlosschleife
	try:
		first_number = raw_input ("Bitte gib die erste Zahl ein: ")
		first_number = int(first_number)
		second_number = raw_input ("Bitte gib eine zweite Zahl ein:  ")
		second_number = int(second_number)
		if first_number > second_number:
			print ("Die groesste Zahl, die Du eingegeben hast ist: "+str(first_number))
			break
		elif second_number > first_number:
			print ("Die groesste Zahl, die Du eingegeben hast ist: "+str(second_number))
			break
	except ValueError:
		print("Bitte gib eine natuerliche Zahl groesser Null ein.")

