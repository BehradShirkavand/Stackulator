def precedence(opt1, opt2):
    if opt1 == opt2:
        return False
    if (opt1 == '*' or opt1 == '/') and (opt2 == '+' or opt2 == '-'):
        return True
    if (opt1 == '+' or opt1 == '-') and (opt2 == '*' or opt2 == '/'):
        return False
    if (opt1 == '+' or opt1 == '-' or opt1 == '/' or opt1 == '*') and (opt2 == '('):
        return True