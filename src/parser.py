import re
import math

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class ExpressionParser:
    def __init__(self):
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'left'},
            '-': {'precedence': 1, 'associativity': 'left'},
            '*': {'precedence': 2, 'associativity': 'left'},
            '/': {'precedence': 2, 'associativity': 'left'},
            '**': {'precedence': 3, 'associativity': 'right'},
            '^': {'precedence': 3, 'associativity': 'right'}
        }
    
    def tokenize(self, expression):
        """Convert expression string into list of tokens"""
        tokens = []
        i = 0
        expression = expression.strip()
        
        while i < len(expression):
            # Skip whitespace
            if expression[i].isspace():
                i += 1
                continue
            
            # Numbers (including decimals)
            if expression[i].isdigit() or expression[i] == '.':
                num_str = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                tokens.append(Token('NUMBER', float(num_str)))
                continue
            
            # Two-character operators
            if i < len(expression) - 1 and expression[i:i+2] == '**':
                tokens.append(Token('OPERATOR', '**'))
                i += 2
                continue
            
            # Single-character operators
            if expression[i] in '+-*/^':
                tokens.append(Token('OPERATOR', expression[i]))
                i += 1
                continue
            
            # Parentheses
            if expression[i] == '(':
                tokens.append(Token('LPAREN', '('))
                i += 1
                continue
            
            if expression[i] == ')':
                tokens.append(Token('RPAREN', ')'))
                i += 1
                continue
            
            # Scientific notation 'e'
            if expression[i] == 'e':
                tokens.append(Token('OPERATOR', '*'))
                tokens.append(Token('NUMBER', 10))
                tokens.append(Token('OPERATOR', '**'))
                i += 1
                continue
            
            raise ValueError(f"Invalid character: {expression[i]}")
        
        return tokens
    
    def infix_to_postfix(self, tokens):
        """Convert infix notation to postfix using Shunting Yard algorithm"""
        output = []
        operator_stack = []
        
        for token in tokens:
            if token.type == 'NUMBER':
                output.append(token)
            
            elif token.type == 'OPERATOR':
                while (operator_stack and 
                       operator_stack[-1].type == 'OPERATOR' and
                       ((self.operators[token.value]['associativity'] == 'left' and
                         self.operators[token.value]['precedence'] <= self.operators[operator_stack[-1].value]['precedence']) or
                        (self.operators[token.value]['associativity'] == 'right' and
                         self.operators[token.value]['precedence'] < self.operators[operator_stack[-1].value]['precedence']))):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            
            elif token.type == 'LPAREN':
                operator_stack.append(token)
            
            elif token.type == 'RPAREN':
                while operator_stack and operator_stack[-1].type != 'LPAREN':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()  # Remove the '('
        
        while operator_stack:
            if operator_stack[-1].type in ['LPAREN', 'RPAREN']:
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())
        
        return output
    
    def evaluate_postfix(self, postfix_tokens):
        """Evaluate postfix expression"""
        stack = []
        
        for token in postfix_tokens:
            if token.type == 'NUMBER':
                stack.append(token.value)
            
            elif token.type == 'OPERATOR':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                
                b = stack.pop()
                a = stack.pop()
                
                if token.value == '+':
                    result = a + b
                elif token.value == '-':
                    result = a - b
                elif token.value == '*':
                    result = a * b
                elif token.value == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = a / b
                elif token.value == '**' or token.value == '^':
                    result = a ** b
                else:
                    raise ValueError(f"Unknown operator: {token.value}")
                
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        
        return stack[0]
    
    def parse_and_evaluate(self, expression):
        """Parse and evaluate an infix expression"""
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix)
        return result
