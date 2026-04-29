"""Calculator maodule"""
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def log(a, base=10):
    """Log one number"""
    if a <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base")
    return math.log(a, base)

def square(a,b):
    """Square two numbers"""
    return a ** b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Не можна ділити на 0"
    return a / b

if __name__== "__main__":

    print("Оберіть операцію: +, -, *, /,**, log")
    operation = input("Введіть операцію: ")
    
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    
    if operation == "+":
        print("Результат:", add(num1, num2))
    elif operation == "-":
        print("Результат:", subtract(num1, num2))
    elif operation == "*":
        print("Результат:", multiply(num1, num2))
    elif operation == "/":
        print("Результат:", divide(num1, num2))
    elif operation == "**":
        print("Результат:", square(num1,num2))
    elif operation == "log":
        print("Результат:", log(num1))
    else:
        print("Невідома операція")
