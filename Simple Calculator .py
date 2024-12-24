# Simple Calculator Program in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit"'\n')

def main():
    while True:
        display_menu()

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
   
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values."'\n')
            continue

        if choice == '1':
            print(f"The Answer = {add(num1, num2,)}"'\n')
        elif choice == '2':
            print(f"The Answer = {subtract(num1, num2)}"'\n')
        elif choice == '3':
            print(f"The Answer = {multiply(num1, num2)}"'\n')
        elif choice == '4':
            print(f"The Answer = {divide(num1, num2)}"'\n')
        else:
            print("Invalid input! Please choose a valid operation."'\n')

if __name__ == "__main__":
    main()
