# 두 수와 연산자(+, -, *, /)를 인자로 받아 계산하는 calculator 함수를 작성하세요.  

def calculator(a, b, op):
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b != 0:
            res = a / b
    print(a,op,b,'=',res)

# Example usage
result = calculator(1, 3, '+')
