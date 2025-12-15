
# Todo Building a Standard Calculator.
# Todo Make all 4 functions.
# Todo Put all 4 functions into same dictionary.
# Todo Use dictionary operations to perform operation
# Todo Make a continuation with same equation option or start over option
#* Solution starts on line 100




























































































def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
} 

def calculator():
    same_equation = True
    num1 = float(input("What is the first number in your equation? "))

    while same_equation:    
        for symbol in math:
            print(symbol)
        operation = input("Pick an operation: '+', '-' ,'*', '/' :  ")
        num2 = float(input("What is your next number in your equation? "))
        answer = math[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'yes' to continue with {answer}, or type 'no' to start over: ")

        if choice == "yes":
            num1 = answer
        else:
            same_equation = False
            print("\n" * 25)
            calculator()

calculator()
