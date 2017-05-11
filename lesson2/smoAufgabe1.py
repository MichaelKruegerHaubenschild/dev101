import sys
import datetime


print ""
print "Talk to me"
print "=========="
print

# ask user for name
q = raw_input("Please enter your first name: ")
print "Thank you, " + q + "."
print

# ask user for his age and birthday
p = input("How old are you? ")

if int(p) == 39:
    print str(p) + "!!! Just like me."
print
c = raw_input("Did you celebrate your birthday this year already? (y/n): ")

#calculate his year of birth
if c == "y":
    print "Congratulations!"
    birth = datetime.datetime.now().year - int(p)
else:
    print "Don't forget to invite me."
    birth = datetime.datetime.now().year - int(p) - 1
    
print    
#give out the year of 100th birthday
print q + ", your 100th birthday is in " + str(birth + 100) + "."
print
print "See you soon."
print


