import datetime


print "\n"*5
print "Talk to me"
print "==========\n\n"


# ask user for name
userName = raw_input("Please enter your first name: ")
print "Nice talking to you, " + userName + ". \n"


# ask user for his age
while True:
    try:
        userAge = int(raw_input("How old are you? "))
    except ValueError:
        print "I didn't get it. Write numbers."
        continue
    else:
        if userAge < 0:
            print "You must be kiddin' me. Try again."
            continue
        else:
            break


# check if age ist even or odd
# task 3 of lesson 2
if userAge % 2 == 0:
    print "Cool! Everything nice and even.\n"
else:
    print str(userAge) + "!!! That's odd.\n"


# calculate user's year of birth
# print out a phrase as often as the age typed in (task 2 of lesson 2)
c = raw_input("Did you celebrate your birthday this year already? [Y/n]: ")
if c.lower() in ('', 'y', 'ye', 'yes'):
    print "Congratulations! " * userAge
else:
    print "Don't forget to invite me. " * userAge
    userAge = userAge + 1
        
celebrate100 = datetime.datetime.now().year + 100 - userAge
    
  
# print out the year of 100th birthday
# task 1 of lesson 2
print "\n" + userName + ", your 100th birthday is in " + str(celebrate100) + ".\n\nSee you at your party!\n\n"