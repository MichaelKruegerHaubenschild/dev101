def greet (name, BeNice):
    if BeNice == True:
        reply = name + ", you are nice!"
    else:
        reply = name + ", you are not so nice!"
    return reply

def mult (text, how_often):
    mult = how_often * text
    return  mult

def listinfo (mylist):
    length = len(mylist)
    print "This is a list. The length is " + str(length)
    print " the first element is: " + str(mylist[0])
    print " the last one is: " + str(mylist[length -1])
    return "Hallo"

mylist = [1,2,3,4,5]
listinfo ([1,2,3,4,5])
