def calc(input):
    signs = '+-/*'
    for sign in signs:
        if sign in input:
            try:
                a, b = input.split(sign)
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
                raise ValueError("Wrong input")
if __name__ == '__main__':
    calc('')
