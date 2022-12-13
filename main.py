def calc(expression):
    allowed = '+-/*'
    if sign in allowed:
        try:
            a, b = expression.split(sign)
            a, b = int(a), int(b)
            if sign == '+':
                return a+b
            if sign == '-':
                return a-b
            if sign == '/':
                return a/b
            if sign == '*':
                return a*b
        except(ValueError, TypeError):
            raise ValueError("Некорректный ввод")
if __name__ == '__main__':
    calc('')
