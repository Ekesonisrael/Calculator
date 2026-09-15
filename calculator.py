import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)


def sine(x):
    # x is expected in degrees, math.sin wants radians
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


def log(x, base=10):
    if x <= 0:
        raise ValueError("Cannot take log of zero or a negative number")
    return math.log(x, base)


def natural_log(x):
    if x <= 0:
        raise ValueError("Cannot take ln of zero or a negative number")
    return math.log(x)


def get_number(prompt):
    # Keeps asking until the user gives a valid number
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("That's not a valid number. Try again.")


def show_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine (degrees)")
    print("8. Cosine (degrees)")
    print("9. Tangent (degrees)")
    print("10. Log base 10")
    print("11. Natural Log (ln)")
    print("0. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye.")
            break

        try:
            if choice == "1":
                x = get_number("Enter first number: ")
                y = get_number("Enter second number: ")
                print(f"Result: {add(x, y)}")
            elif choice == "2":
                x = get_number("Enter first number: ")
                y = get_number("Enter second number: ")
                print(f"Result: {subtract(x, y)}")
            elif choice == "3":
                x = get_number("Enter first number: ")
                y = get_number("Enter second number: ")
                print(f"Result: {multiply(x, y)}")
            elif choice == "4":
                x = get_number("Enter first number: ")
                y = get_number("Enter second number: ")
                print(f"Result: {divide(x, y)}")
            elif choice == "5":
                x = get_number("Enter base: ")
                y = get_number("Enter exponent: ")
                print(f"Result: {power(x, y)}")
            elif choice == "6":
                x = get_number("Enter number: ")
                print(f"Result: {square_root(x)}")
            elif choice == "7":
                x = get_number("Enter angle in degrees: ")
                print(f"Result: {sine(x)}")
            elif choice == "8":
                x = get_number("Enter angle in degrees: ")
                print(f"Result: {cosine(x)}")
            elif choice == "9":
                x = get_number("Enter angle in degrees: ")
                print(f"Result: {tangent(x)}")
            elif choice == "10":
                x = get_number("Enter number: ")
                print(f"Result: {log(x)}")
            elif choice == "11":
                x = get_number("Enter number: ")
                print(f"Result: {natural_log(x)}")
            else:
                print("Invalid option. Pick a number from the menu.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
