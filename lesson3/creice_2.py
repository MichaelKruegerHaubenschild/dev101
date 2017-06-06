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


while True:
	try:
		operator = raw_input ("Bitte gib eine 1 (x) oder eine 2 (/) ein: ")
		operator = int(operator)
		if operator == 1:
			ergebnis = first_number*second_number
			print ("Das Ergebnis ist ") + str(ergebnis)
			break
		elif operator == 2: 
			ergebnis = first_number/second_number
			print ("Das Ergebnis ist ") + str(ergebnis)
			break
		else:
			print ("Bitte gib entweder 1 oder 2 ein! ")
			continue
	except ValueError:
		print("Bitte gib entweder 1 oder 2 ein.")
