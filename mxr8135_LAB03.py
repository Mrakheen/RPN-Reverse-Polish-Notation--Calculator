# UTA ID : 1001848135
# Name : Mubtasim Ahmed Rakheen
# Date : 7/24/2024
# OS Used : Windows, Linux

import os

def evaluate_rpn(expression):
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }
    
    for token in expression.split():
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
    input_file_path = os.path.join(script_dir, 'input_RPN.txt')
    
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line:
            result = evaluate_rpn(line)
            print(result)

if __name__ == '__main__':
    main()












