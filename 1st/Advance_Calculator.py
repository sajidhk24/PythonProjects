def sum(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    return n1/n2


def mult(n1, n2):
    return n1 * n2


operations = {
    '+': 'sum',
    '-': 'sub',
    '/': 'div',
    '*': 'mult',
            }

n1 = int(input('Enter the first number n1: '))
n2 = int(input('Enter the second number n2: '))
for symbol in operations:
    print(symbol)
operations_symbol = input('Enter the operation symbol: ')
calculation_function = operations[operations_symbol]
print(operations[operations_symbol])
answer = calculation_function(n1, n2)
print(type(calculation_function))
print(f"{n1} {operations_symbol} {n2} '=' {answer}")