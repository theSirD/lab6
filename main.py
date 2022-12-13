def calc(a, b, sign):
    allowed = '+-/*'
    if sign in allowed:
        try:
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
    calcul('')
