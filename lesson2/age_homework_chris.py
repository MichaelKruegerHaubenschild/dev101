## Homework 1
## Autor: Christian Driesen
##

while True: ## ist eine Endlosschleife
	try:
		age = input ("Bitte gib Dein Alter ein: ")
		age = int(age)
		if age <0:
			print ("Die Zahl muss groesser 0 sein! Versuche es noch ein Mal!")
			continue
		else:
			break
	except ValueError:
		print("Bitte gib eine natuerliche Zahl groesser Null ein.")

while True:
	try:
		bday_happen = input ("Hattest Du schon Geburtstag (j/n)   ")
		if bday_happen in ['j','n']:
			break
		else:
			print ("Bitte gib j oder n ein ")
			continue
	except ValueError:
		print ("Bitte gib j oder n ein ")

if bday_happen =='j':
	hundreds_bday = 100-age+2017
else:
	hundreds_bday = 100-age+2016
print ("Dein Hundertster Geburtstag ist im Jahr  ",hundreds_bday)

