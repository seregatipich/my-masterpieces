import math


def sum(a, b):
    result = a + b
    return result


def substract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result


def exponentiate(a, b):
    result = a ** b
    return result


def sqrRoot(a):
    result = math.sqrt(a)
    return result


def operationRequest():
    message = '''Choose required operation:
    +
    -
    *
    /
    **
    sqrRoot (Enter first number, set second to zero)
    
    Вы выбрали:
    '''
    operation = input(message)
    return operation


def compute(a, b, operation):
    if operation == '+':
        result = sum(a, b)
    elif operation == '-':
        result = substract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    elif operation == '**':
        result = exponentiate(a, b)
    elif operation == 'sqrRoot':
        result = sqrRoot(a)
    else:
        print('Unknown operation')

    return result


def calculate():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))

    operation = operationRequest()
    result = compute(a, b, operation)

    print(f'Result: {result}')


calculate()
