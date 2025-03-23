# Function to perform the mathematical operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Main program
def main():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to input the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the calculation
    result = calculate(num1, num2, operation)
    
    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

