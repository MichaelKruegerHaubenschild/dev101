counter = 0
ungerade = 0
liste = [3,1,3,5,7,9]

for i in liste:
        if i%2 == 1:
            counter = counter + 1
        if counter == 6:
            ungerade = ungerade + 1
print counter
print ungerade
