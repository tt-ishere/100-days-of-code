# calculator
from art import logo

# Add 
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2 

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
}

def calculator():
    print(logo) 
    num1 = float(input("Enter the first number: "))
    # show operations 
    for symbol in operations:
        print(f"{symbol} \n")
    should_continue = True   
    while should_continue:
        # pick operation     
        operation_symbol = input("what operation do you want to perform: ")

        num2 = float(input("Enter the next number: "))

        calculate = operations[operation_symbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() #recursion
           
calculator()