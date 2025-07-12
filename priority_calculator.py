def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

def is_operator(character, ops) -> bool:
    for op in ops:
        if character == op:
            return True
    return False

def calc(operand1, operand2, op):
    if op == '+':
        return add(operand1, operand2)
    if op == '-':
        return subtract(operand1, operand2)
    if op == '/':
        return divide(operand1, operand2)
    if op == '*':
        return multiply(operand1, operand2)
    return None

def is_divided_by_zero(a, b, op):
    if b == 0:
        if op == '/':
            raise ValueError

def to_postfix(expression):
    op_priority = {'+': 1, '-': 1, '/': 2, '*': 2}
    postfix_expression = []
    op_stack = []

    for element in expression:
        if element.isdigit() or (element.startswith('-') and element[1:].isdigit()):
            postfix_expression.append(element)
        elif element == '(':
            op_stack.append(element)
        elif element == ')':
            while op_stack and op_stack[-1] != '(':
                postfix_expression.append(op_stack.pop())
            op_stack.pop()
        else: 
            while op_stack and op_stack[-1] != '(' and op_priority.get(op_stack[-1], 0) >= op_priority.get(element, 0):
                postfix_expression.append(op_stack.pop())
            op_stack.append(element)
    while op_stack:
        postfix_expression.append(op_stack.pop())
    return postfix_expression

def priority_calculator(expression):
    num_stack = []
    for element in expression:
        if element.isnumeric():
            num_stack.append(element)
        else:
            operand1 = num_stack.pop()
            operand2 = num_stack.pop()
            try:
                is_divided_by_zero(float(operand2), float(operand1), element)
            except ValueError:
                print("Error: Division by zero.")
                raise ValueError
            num_stack.append(calc(float(operand2), float(operand1), element))
    return float(num_stack.pop())

def bracket_handler(splitted) -> bool:
    bracket_stack = []
    for element in splitted:
        if element == '(':
            bracket_stack.append(element)
        elif element == ')':
            if bracket_stack.pop() != '(':
                return False
    if bracket_stack:
        return False
    return True

def input_organizer(_inputs, ops):
    _inputs = _inputs.strip()
    res = ""
    for idx, element in enumerate(_inputs):
        if is_operator(element, ops):
            res += element + " "
        else:
            temp = ""
            for j in range(idx, len(_inputs)):
                if not is_operator(_inputs[j], ops):
                    temp += _inputs[j]
                else:
                    break
            res += temp + " "
    return res.rstrip()

def check_numerics(_inputs, ops) -> bool:
    for element in _inputs:
        if is_operator(element, ops) == False:
            if not element.isnumeric():
                return False
    return True

def input_hanlder():
    ops = "+-/*()"
    _inputs = input('Enter expression: ')
    _inputs = input_organizer(_inputs, ops).split()
    if len(_inputs) < 2:
        raise ValueError
    if bracket_handler(_inputs) == False:
        raise ValueError
    if not check_numerics(_inputs, ops):
        raise ValueError
    return _inputs

def main():
    splitted = []
    while not splitted:
        try:
            splitted = input_hanlder()
        except ValueError:
            print('Invalid input. (ex: 5 + 4 / 2 * 1)')
    postfix_expression = to_postfix(splitted)
    try:
        res = priority_calculator(postfix_expression)
    except ValueError:
        print("Invalid input.")
        return
    print(f'Result: {res}')

if __name__ == '__main__':
    while 42:
        main() 
