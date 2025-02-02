
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multipication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2



userInput = input("""Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
Enter choice (1/2/3/4/5):""")



try:
    userInputInt = int(userInput)
    if userInputInt < 1 or userInputInt > 5:
            print("Error: Please enter a number between 1 and 5")
    else:
            firstNum = float(input("Enter first number: "))
            secondNum = float(input("Enter second number: "))
            if userInputInt == 4 and secondNum == 0:
                print("You can't divide any number by zero")
            elif userInputInt == 5 and secondNum == 0:
                print("You can't find the modulus when the second number is zero")
            else:
                if userInputInt == 1:
                    result = addition(firstNum, secondNum)
                    print(f"Result = {firstNum} + {secondNum} = {result}")
                elif userInputInt == 2:
                    result = subtraction(firstNum, secondNum)
                    print(f"Result = {firstNum} - {secondNum} = {result}")
                elif userInputInt == 3:
                    result = multipication(firstNum, secondNum)
                    print(f"Result = {firstNum} * {secondNum} = {result}")
                elif userInputInt == 4:
                    result = division(firstNum, secondNum)
                    print(f"Result = {firstNum} / {secondNum} = {result}")
                elif userInputInt == 5:
                    result = modulus(firstNum, secondNum)
                    print(f"Result = {firstNum} % {secondNum} = {result}")

except ValueError:
    print("PLease Enter a Number")


