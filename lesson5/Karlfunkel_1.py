
def greet(name,be_nice):
    if be_nice == True:
        reply = "Hallo " + name + " schoen, das du da bist."
    else:
        reply = "Hallo, " + name + " du sahst auch schon mal besser aus."
    return reply

print greet("Christian", True)
print greet("Christian", False)

#string und wie oft vorkommen soll

def multiply(Ausgabe, a):
    return a * Ausgabe

print multiply("bla",5)
