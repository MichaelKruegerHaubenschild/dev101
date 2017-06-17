#less than 10
from random import randint
num1 = randint(1,20)
num2 = randint(1,20)
num3 = randint(1,20)
num4 = randint(1,20)
num5 = randint(1,20)
num6 = randint(1,20)
ersteliste = [num1, num2, num3, num4, num5, num6]

zweiteliste = []

counter = 0

for element in ersteliste:
    counter = counter + 1
    if element <= 10:
        zweiteliste.append(element)

print zweiteliste
