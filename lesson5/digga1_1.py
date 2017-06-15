def greet (name, BeNice):
    if BeNice == True:
        reply = name + ", you are nice!"
    else:
        reply = name + ", you are not so nice!"
    return reply

print greet("Peter", True)
print greet("Peter", 1)
