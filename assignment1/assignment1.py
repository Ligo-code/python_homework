# Write your code here.
def hello():
    return "Hello!"

print(hello())

def greet(name):
    return f"Hello, {name}!"

print(greet("Niya"))

def calc(num1, num2, operation="multiply"):
    try:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "int_divide":
            return num1 // num2
        elif operation == "power":
            return num1 ** num2
        else:
            return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except (TypeError, ValueError):
        return "You can't multiply those values!"
    
print(calc(10,5,'add')) # 15
print(calc(10,5,'substract')) # 5
print(calc(5,6,'mltiply')) # 50
print(calc(10,5,'divide')) # 2
print(calc(10,5,'modulo')) # 0
print(calc(10,5,'int_divide')) # 2
print(calc(10,5,'exponent')) # 100000
print(calc(10, 0, "divide"))    # You can't divide by 0!
print(calc("a", 5, "multiply")) # You can't multiply those values!
    




