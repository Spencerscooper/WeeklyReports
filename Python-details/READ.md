<!--Python Group Report-->
## This report cover the following topic that was evaluated this week

### Book title Python for everybody
### During last week presentation we talked about Variable, Statement and Expression. To continue we will include the following:

* Variable
* Expression
* Statement
* Python Operators
* and Function
<!--This block of code illustrate a function with the above mentioned-->

numb1 = 30
number2 = 40
```python
def adding_numbers(numb1, number2):
    return numb1+numb1

```
```python
def substracting_numbers(number1, number2):
    return number1 - number2

```
##### Explanation of our code: line 14 & 15 is a variable that the single equal sign in Python mean assignment. The value 30 is an integer, in Python we have datatype and each value belongs to a specific datatype so 30 belong to the Int datatype which mean integer. numb1 & numb1 is a  global variable because it defined outside of the function. According to Python Global variable can be access from any location within the program.

#### Line 17 is a function definition. According to python Dr. Charles in Python for Everybody the "def" is a reserve keyword that defined a function. character after the function is the name of the function, so "adding_numbers is the name of the function. It's advisible to use meaning name when definding function or variable with that it can help you avoid the usage of comment in your code block and make the make programmer and person reading your text to know what the program or block of code is all about. 

### After the name of our function we have a open and close parenthesis that have numb1 and numb2 these value are called the parameter of the value and it end with a semi colon which is the head of the function, and line 18 have a return statement that is indented under our function block. the return statement have numb1 plus numb2. They are consider to be the body of the function that adding two operands. According to Python the plus sign is one of Python Arimethic operator that represent addition. 


## Week II Report March 17, 2023
##Conditional Execution and Function
### According to Python for everybody for programmer to write meaningful program we most have the ability to control our program. In this light we will focus on comparison operators which include !=, <,>, >=, <=, ==, is, AND is not..

### Looking at our below program we were able to develop a simple calculator that will accept input integer number for a user and use either of the arithmetic operator that is being input by the use and give the result after the computation take place. In this program we use a  conditional execution with a chained condition. because our program have five branches four (elif statement) and one else statement. So this program will executive if the value enter by the user meet the requirement, if not the else statement will pop up with the message place in the parenthesis. Going forward acording to python we should already use a meaningful name whether it's a variable or function definition with that it give the next person clue to what is affording wihin the program. So in this function we have a local variable called value1, value2 that is only access by the function.

```python
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
```


