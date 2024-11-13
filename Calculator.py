def get_name():
    name = input("Enter Your Name: ")
    return name

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def power(num1,num2):
    return num1**num2

def modulus(num1,num2):
    return num1%num2

def main():
    name = get_name()

    print(f"Hello {name}!, Welcome to the Calculator Program.")
    print('''Select the type of Operation you want to perform:
    1. Addition(+)
    2. Subtraction(-)
    3. Multiplication(*)
    4. Division(/)
    5. Power(^)
    6. Modular Division(%)
    7. Exit(Enter "quit" to exit the program)''')

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The Sum  of {num1} + {num2} = {add(num1,num2)}")
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The Difference of {num1} - {num2} = {subtract(num1,num2)}")
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The Product of {num1} * {num2} = {multiply(num1,num2)}")
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"The Quotient of {num1} / {num2} = {divide(num1,num2)}")
        elif choice == "5":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"The Power of {num1} ^ {num2} = {power(num1,num2)}")
        elif choice == "6":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"The Remainder of {num1} % {num2} = {modulus(num1,num2)}")
        elif choice.lower() == "quit":
            print("Thank you for using the Calculator Program!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            

main()
