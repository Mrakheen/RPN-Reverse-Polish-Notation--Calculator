# UTA ID : 1001848135
# Name : Mubtasim Ahmed Rakheen
# Date : 7/24/2024
# OS Used : Windows, Linux

import os

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)
    elif operator == '%':
        values.append(left % right)

def to_rpn(expression):
    operators = []
    values = []
    result = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            result.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                result.append(operators.pop())
            operators.pop()  # pop '('
        else:
            while (operators and precedence(operators[-1]) >= precedence(token)):
                result.append(operators.pop())
            operators.append(token)
    
    while operators:
        result.append(operators.pop())
    
    return ' '.join(result)

def evaluate_rpn(rpn_expression):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b,
    }
    
    for token in rpn_expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]

def main():
    # Get the path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, 'input_RPN_EC.txt')
    
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line:
            rpn_expression = to_rpn(line)
            result = evaluate_rpn(rpn_expression)
            print(rpn_expression)
            print(result)

if __name__ == '__main__':
    main()









