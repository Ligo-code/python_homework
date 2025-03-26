# Write your code here.
def hello():
    return "Hello!"

print(hello())

def greet(name):
    return f"Hello, {name}!"

print(greet("Niya"))

'''def calc(num1, num2, operation="multiply"):
    try:
                # check num1, num2 - numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return "You can't multiply those values!"
        
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
print(calc(10,5,'subtract')) # 5
print(calc(5,6,'multiply')) # 50
print(calc(10,5,'divide')) # 2
print(calc(10,5,'modulo')) # 0
print(calc(10,5,'int_divide')) # 2
print(calc(10,5,'power')) # 100000
print(calc(10, 0, "divide"))    # You can't divide by 0!
print(calc("a", 5, "multiply")) # You can't multiply those values!'''

def calc(num1, num2, operation="multiply"):
    try:
        # check num1, num2 - numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return "You can't multiply those values!"

        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except (TypeError, ValueError):
        return "You can't multiply those values!"

# Tests
print(calc(10, 5, 'add'))        # 15
print(calc(10, 5, 'subtract'))   # 5
print(calc(5, 6, 'multiply'))    # 30
print(calc(10, 5, 'divide'))     # 2.0
print(calc(10, 5, 'modulo'))     # 0
print(calc(10, 5, 'int_divide')) # 2
print(calc(10, 5, 'power'))      # 100000
print(calc(10, 0, 'divide'))     # You can't divide by 0!
print(calc("a", 5, 'multiply'))  # You can't multiply those values!
    

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return "Invalid data type!"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion("123", "int"))   
print(data_type_conversion("123.45", "float"))  
print(data_type_conversion(123, "str"))      
print(data_type_conversion("abc", "int"))    



def grade(*args):
    try: 
        if not all(isinstance(score,(int, float)) for score in args):
            return "Invalid data was provided."
        if len(args) == 0:
            return "Invalid data was provided."
        
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        
    except (TypeError, ValueError):
        return "Invalid data was provided."

print(grade(95,85,76))
print(grade(90,98))
print(grade(60,65))
print(grade(70,71))
print(grade(50,51))
print(grade("b",98))
print(grade())

'''def repeat(string, count):
    try:
        if not isinstance(count, int) or count < 0:
            return "Invalid count value."
        result = ""
        for _ in range(count):
            result += string
        return result
    except Exception as e:
        return f"An error accured: {str(e)}"

print(repeat("a", 5))
print(repeat("fizz",2))
print(repeat("buzz","3"))
print(repeat("abc", 0))
print(repeat("boo", -1))'''

def repeat(string, count):
    try:
        if not isinstance(string, str):
            return "Invalid string value."
        
        if isinstance(count, str)and count.isdigit():
            count = int(count)

        if not isinstance(count, int) or count < 0:
            return "Invalid count value."

        match count:
            case 0:
                return ""
            case 1:
                return string
            case _:
                return string * count
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Примеры
print(repeat("a", 5))        # aaaaa
print(repeat("fizz", 2))     # fizzfizz
print(repeat("buzz", "3"))   # Invalid count value.
print(repeat("abc", 0))      # (пустая строка)
print(repeat("boo", -1))     # Invalid count value.


def student_scores(option, **kwargs):
    try:
        if not kwargs or not all(isinstance(score, (int, float)) for score in kwargs.values()):
            return "No valid scores provided"
        if option == "best":
            return max(kwargs, key=kwargs.get)
        elif option == "mean": 
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid option"
        
    except Exception as e:
        return f"An error accured: {str(e)}"
    
print(student_scores("best", Nika=98, Den=85, Niya=100))   
print(student_scores("mean", Nika=68, Den=85, Niya=100))  
print(student_scores("best"))  
print(student_scores("mean", Nika="B", Den=85, Niya=100))  
print(student_scores("great", Nika=98, Den=85, Niya=100))  


def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

    try:
        words = text.split()

        if not words:
            return ""
        
        for i, word in enumerate(words):
            if i == 0 or i == len(words)-1:
                words[i] = word.capitalize()
            elif word.lower() in little_words:
                words[i] = word.lower()
            else:
                words[i] = word.capitalize()

        return " ".join(words)
    
    except Exception as e:
        return f"An error accured: {str(e)}"
    
print(titleize("the lord of the rings"))
print(titleize("a tale of two cities"))
print(titleize("on the road"))
print(titleize("master & margarita"))
print(titleize(""))
print(titleize("b"))


def hangman(secret, guess):
    try:
        result = ""

        for char in secret:
            if char in guess:
                result += char
            else:
                result += "_"
        return result
    
    except Exception as e:
        return f"An error accured: {str(e)}"
    
print(hangman("alphabet", "ab"))   
print(hangman("programming", "pg")) 
print(hangman("python", "xyz"))       
print(hangman("hello", "ello")) 
print(hangman("hello", "")) 
print(hangman("", "xyz")) 


def pig_latin(sentence):
    vowels = {"a", "e", "i", "o", "u"}
    result = []

    try:
        words = sentence.lower().split()

        for word in words:
            if word[0] in vowels:
                result.append(word+"ay")
            elif word.startswith("qu"):
                result.append(word[2:]+"quay")
            elif word[1:3] == "qu":
                result.append(word[3:] + word[:3] + "ay")
            else:
                for i, char in enumerate(word):
                    if char in vowels:
                        result.append(word[i:]+word[:i]+"ay")
                        break
                else:
                    result.append(word+"ay")

        return " ".join(result)
    
    except Exception as e:
        return f"An error occured: {str(e)}"
    
print(pig_latin("hello world"))
print(pig_latin("apple pie"))
print(pig_latin("time is money") )
print(pig_latin("Python is fun"))
print(pig_latin(""))    



