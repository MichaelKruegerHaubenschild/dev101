## Homework 1
## Autor: Christian Driesen
##

while True:
    try:
        age = raw_input("Bitte gib Dein Alter ein: ")
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
		bday_happen = raw_input ("Hattest Du schon Geburtstag (j/n)   ")
		if bday_happen in ['j','n']:
			break
		else:
			print ("Bitte gib j oder n ein ")
		continue

if bday_happen =='j':	
	hundreds_bday = 100-age+2016
else:
	hundreds_bday = 100-age+2017

print (hundreds_bday)


