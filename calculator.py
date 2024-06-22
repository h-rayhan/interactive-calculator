import os
from art import logo

print(logo)

def clear():
    """Clears the console screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

# Define the arithmetic functions
def addition(a, b):
    """Takes two inputs and returns the result by performing addition."""
    return a + b

def subtraction(a, b):
    """Takes two inputs and returns the result by performing subtraction."""
    return a - b

def division(a, b):
    """Takes two inputs and returns the result by performing division."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def multiplication(a, b):
    """Takes two inputs and returns the result by performing multiplication."""
    return a * b

# Create a dictionary that maps operation symbols to corresponding functions
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

# Function to prompt the user for a number, with input validation
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nPlease enter a valid number\n")

# Function to prompt the user for an operation, with input validation
def get_operation():
    while True:
        # Display available operations
        print("\n".join(operations.keys()))
        operation = input("\nPick an operation: ").strip()
        if operation in operations:
            return operation
        print("\nPlease enter a correct symbol\n")

# Function to perform the calculation process
def calculate():
    # Prompt for the first number
    x = get_number("Enter first number: ")

    while True:
        # Prompt for the operation and the second number
        operation = get_operation()
        y = get_number("\nEnter second number: ")

        # Perform the selected operation
        result = operations[operation](x, y)

        # Check if the result is an error message (string) or a valid result
        if isinstance(result, str):
            print(f"\n{result}\n")
        else:
            print(f"\n{x} {operation} {y} = {result}\n")

        # Ask the user if they want to continue with the current result, start a new calculation, or exit
        while True:
            print(f"Type 'y' to continue with the current result {result}")
            print("Type 'n' to start a new calculation")
            print("Alternatively, type any other key to exit\n")
            continue_calc = input().strip().lower()
            clear()
            if continue_calc in ['y', 'yes', 'continue']:
                x = result
                break
            return continue_calc in ['n', 'new']

# Main loop to keep the calculator running until the user chooses to exit
while calculate():
    pass

# Print a goodbye message when the user exits
print("Goodbye!")
