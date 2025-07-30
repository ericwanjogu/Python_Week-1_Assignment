#Creating a simple Python program that asks the user to input two numbers;
#and a mathematical operation (addition, subtraction, multiplication, or division);

num1 = float(input("Key in first number: "))
operation = input("Choose an operation (+, -, /, *): ")
num2 = float(input("Key in second number: "))

#Running the calculation
if operation == "+":
    sum = num1 + num2
    print("Result:", sum)
elif operation == "-":
    subtraction = num1 - num2
    print("Result:", subtraction)
elif operation == "*":
    multiplication = num1 * num2
    print("Result:", multiplication)
elif operation == "/":
    if num2 != 0 :
        division = num1 / num2
        print("Result:", division)
    else:
        print("Error: DIVISION BY ZERO NOT PERMITTED.")
else:
        print("INVALID OPERATION, USE +, -, *, /.")