def check_bracket(input_str):
    stack = []
    output = [' '] * len(input_str)
    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i) #把左括号的位置亚入栈中
        elif char == ')':
            if stack: #右括号和左括号位置有对应
                output[stack.pop()] = ' ' #左括号位置为空
                output[i] = ' '   #右括号位置为空
            else:
                output[i] = '?'  #没有左括号对应，右括号位置打？
    while stack:
        output[stack.pop()] = 'x' #没有右括号对应，左括号位置打x
    return ''.join(output)

test_cases = [
    "bge))))))))))",
    "((IIII)))))))",
    "()()()()(uuu",
    "))))UUUU((()"]

for case in test_cases:
    print(case)
    print(check_bracket(case))