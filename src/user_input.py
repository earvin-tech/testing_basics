from src.calculator import add

def get_user_input_and_double():
    num = int(input("Enter a number: "))
    double_value = add(num,num)
    return double_value

def get_user_inputs_and_add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = add(num1, num2)
    return sum
