def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "The second number cannot be zero as that would involve division by zero."
    return a / b


def display_menu():
    print("\nSimple Calculator")
    print("------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Please do not enter letters or characters - only numbers")


def calculator():
    while True:
        display_menu()
        choice = input("Select an operation (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Please choose from one of the four numerical options listed above.")
            continue

        num1, num2 = get_numbers()

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

        input("\nPress Enter to continue")

if __name__ == "__main__":
    calculator()