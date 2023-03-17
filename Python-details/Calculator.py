#Simple calculator with the Arithmetic operator learn so far


def calculation(value1, value2):
    print("Welcome to Python group simple calculator")
    
    if ops == '+': 
        print("Your answer is", value1 + value2)
        
    elif ops == '-':
        print("Your answer for sub is:", value1-value2)
    elif ops == '/':
        print("You answer for division is", value1/value2)
    elif ops == '%':
        print("Your answer for float division is", value1%value2)
    elif ops == '//':
        print("Your answer for modulus is", value1//value2)

    else:
        print("Invalue operator!!!")
    

value1 = int(input("Enter a value \n"))
value2 = int(input("Enter another value \n"))
ops = input("Enter a operator \n")

calculation(value1, value2)
