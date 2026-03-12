#File Read multiple exceptions 

file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except IOError:
    print(f"An error occurred while reading the file '{file_name}'.")