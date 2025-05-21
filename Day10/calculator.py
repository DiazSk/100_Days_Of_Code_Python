logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

math_operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator(previous_result=None):
    if previous_result is not None:
        num1 = previous_result
        print(f"Previous result: {num1}")
    else:
        num1 = float(input("Enter the first number: "))

    operation = input("Enter the operation (+, -, * or /): ")
    num2 = float(input("Enter the second number: "))

    if operation in math_operators:
        result = math_operators[operation](num1, num2)
        print(f"The result of {num1} {operation} {num2} is {result}")
        
        # Ask if user wants to continue with this result
        keep_going = input("\nDo you want to continue with the previous result? (y/n) or type 'exit' to quit: ")
        if keep_going.lower() == "y":
            return calculator(result)
        elif keep_going.lower() == "exit":
            print("Thank you for using the calculator!")
            return result
        else:
            return calculator()
    else:
        print("Invalid operation")
        return calculator(num1)

# Start the calculator with recursive calls
calculator()





