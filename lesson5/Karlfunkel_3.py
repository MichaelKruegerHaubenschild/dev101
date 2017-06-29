print "Hello World"

def list_function(liste):
    neu = liste * 3
    return neu

my_list = [1, 39, 49, 32, 394, -100]

counter = 0
for element in my_list:

    counter = counter + 1
    if counter == 3:
        print "Auto"
    else:
        print element

print "End"

result = list_function(my_list)
print result
