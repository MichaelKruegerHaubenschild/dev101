from datetime import datetime

print "Hello World"
name = raw_input("whats your name? ")
print "Welcome " +name
age = input("How old are you?: ")
print "Hello " + name +"! You are " + str(age) + " years old."
currentYear = datetime.now().year
Year = currentYear -age + 100
print "You will turn 100 in the year " + str(Year)
