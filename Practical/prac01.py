def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum =", a + b)

def find_max():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    max_val = max(a, b)
    print("Maximum value =", max_val)

def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

while True:
    print("\nMenu:")
    print("1. Add two numbers")
    print("2. Find maximum of two numbers")
    print("3. Check if a number is even or odd")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_numbers()
    elif choice == '2':
        find_max()
    elif choice == '3':
        check_even_odd()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")