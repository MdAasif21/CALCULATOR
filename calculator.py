def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the simple calculator!")
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of division: {result}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
