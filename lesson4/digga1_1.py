def my_max(number1,number2,number3):
    if number1 > number2 and number1 > number3:
        new = number1
    elif number2 > number3 and number2 > number1:
        new = number2
    else:
        new = number3
    return new


number1 = input("Please enter an number: ")
number2 = input("Please enter an number: ")
number3 = input("Please enter an number: ")

highest = my_max(number1,number2,number3)
print highest
