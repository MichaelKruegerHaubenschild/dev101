import datetime


print "\n"*3
print "Talk to me"
print "==========\n\n"

# ask user for name
q = raw_input("Please enter your first name: ")
print "Thank you, " + q + ". \n"


# ask user for his age and birthday
p = input("How old are you? ")

# check if age ist even or odd
# task 3 of lesson 2
if int(p) % 2 == 0:
    ageComment = "Cool! That's EVEN better."
else:
    ageComment= str(p) + "!!! That's odd"
    if int(p) == 39:
        ageComment = ageComment + " and just like me."
    else:
        ageComment = ageComment + "."
print ageComment + "\n"

c = raw_input("Did you celebrate your birthday this year already? (y/n): ")

# calculate user's year of birth
# print out a phrase as often as a number typed in (task 2 of lesson 2)
print "\n"
if c == "y":
    print "Congratulations! " * int(p)
    birth = datetime.datetime.now().year - int(p)
else:
    print "Don't forget to invite me. " * int(p)
    birth = datetime.datetime.now().year - int(p) - 1
    
  
# give out the year of 100th birthday
# task 1 of lesson 2
print "\n" + q + ", your 100th birthday is in " + str(birth + 100) + ".\n\nSee at your party!\n\n"