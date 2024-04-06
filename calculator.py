print("1 - ADDITION")
print("2 - SUBTRACTION")
print("3 - MULTIPLICATION")
print("4 - DIVISION")
option = int(input(" choose an option:"))

if(option in [1,2,3,4]):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2 
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2
    
else:
    print("invalid operation entered")

print(" the result of the operation is {}".format(result))

