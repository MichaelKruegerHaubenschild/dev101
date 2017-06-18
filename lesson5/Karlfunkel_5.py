#less than 10
from random import randint

ersteliste = []
while len(ersteliste) < 30:
    ersteliste.append(randint(1,20))

zweiteliste = []
counter = 0
for element in ersteliste:
    counter = counter + 1
    if element <= 10:
        zweiteliste.append(element)

print zweiteliste
