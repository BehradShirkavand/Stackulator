from stack import Stack
from precedence import precedence
from str_reverse import str_reverse

operator = ['+', '-', '*', '/', '(', ')']

class Expression:
    
    def __init__(self, expression):
        self.expression = expression
        
    def get_postfix(self):
        stack = Stack()
        postfix_expression = ''
        for i in range(len(self.expression)):
            if self.expression[i] in operator:
                if self.expression[i] == '(':
                    stack.push(self.expression[i])
                elif self.expression[i] == ')':
                    while not stack.is_empty():
                        if stack.peek() != '(':
                            postfix_expression += stack.pop()+' '
                        else:                   
                            stack.pop()
                            break
                elif self.expression[i] == '-':
                    if stack.is_empty():
                        if postfix_expression == '':
                            postfix_expression += '-'
                        else:
                            stack.push('-')
                    else:
                        if self.expression[i-1] in operator and self.expression[i-1] != ')':
                            postfix_expression += '-'
                        else:
                            if precedence(self.expression[i], stack.peek()):
                                stack.push(self.expression[i])
                            else:
                                postfix_expression += stack.pop()+' '
                                stack.push(self.expression[i])
                else:
                    if not stack.is_empty():
                        if precedence(self.expression[i], stack.peek()):
                            stack.push(self.expression[i])
                        else:
                            postfix_expression += stack.pop()+' '
                            stack.push(self.expression[i])
                    else:
                        stack.push(self.expression[i])
            else:
                postfix_expression += self.expression[i]+' '

        while not stack.is_empty():
            if stack.peek() != '(':
                postfix_expression += stack.pop()+' '
            else:
                stack.pop()
        
        self.expression = postfix_expression
        return self.expression

    def get_prefix(self, expression):
        self.expression = str_reverse(self.expression)
        return self.expression
    # def get_prefix(self):
    #     operator_stack = Stack()
    #     operand_stack = Stack()
    #     for i in range(len(self.expression)):
    #         if self.expression[i] in operator:
    #             if self.expression[i] == '(':
    #                     operator_stack.push(self.expression[i])

    #             elif self.expression[i] == ')':
    #                 while not operator_stack.is_empty():
    #                     if operator_stack.peek() != '(':
    #                         opt = operator_stack.pop()
    #                         x = operand_stack.pop()
    #                         y = operand_stack.pop()
    #                         temp = opt + ' '+ y+ ' ' + x + ' '
    #                         operand_stack.push(temp)        
    #                     else:
    #                         operator_stack.pop()
    #                         break
    #             else:
    #                 while not operator_stack.is_empty() and not precedence(self.expression[i], operator_stack.peek()):
    #                     opt = operator_stack.pop()
    #                     x = operand_stack.pop()
    #                     y = operand_stack.pop()
    #                     temp = opt + ' '+ y+ ' ' + x + ' '
    #                     operand_stack.push(temp)
    #                 operator_stack.push(self.expression[i])
    #         else:
    #             operand_stack.push(self.expression[i])
    #     while not operator_stack.is_empty():
    #         opt = operator_stack.pop()
    #         x = operand_stack.pop()
    #         y = operand_stack.pop()
    #         temp = opt + ' '+ y+ ' ' + x + ' '
    #         operand_stack.push(temp)
    #     return operand_stack.peek()

    def get_evaluate(self, expression):
        stack = Stack()
        self.expression = self.expression.split()
        for i in range(len(self.expression)):
            if not self.expression[i] in operator:
                stack.push(self.expression[i])
            else:
                if self.expression[i] == '+':
                    x = float(stack.pop())
                    y = float(stack.pop())
                    stack.push(y+x)
                if self.expression[i] == '-':
                    x = float(stack.pop())
                    y = float(stack.pop())
                    stack.push(y-x)
                if self.expression[i] == '*':
                    x = float(stack.pop())
                    y = float(stack.pop()) 
                    stack.push(y*x) 
                if self.expression[i] == '/':
                    x = float(stack.pop())
                    y = float(stack.pop()) 
                    stack.push(y/x)
        return stack.peek()