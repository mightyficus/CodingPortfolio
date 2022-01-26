# postfixfix.py

def precedence(char1, char2):
    if char1 == '+' or char1 == '-':
        if char2 == '(' or char2 == ')' or char2 == '+' or char2 == '-':
            return True
        else:
            return False
    elif char1 == '*' or char1 == '/':
        if char2 == '(' or char2 == ')' or char2 == '+' or char2 == '-' or char2 == '*' or char2 == '/':
            return True
        else:
            return False
    elif char1 == '^':
        if char2 in {'(',')','+','-','*','^'}:
            return True
        else:
            return False
    

def postfix(calcString):
    poststring = '(' + calcString + ')'
    charstack = []
    output = ''
    for char in poststring:
        if char.isdigit():
            output = output + char
        elif char == '(':
            charstack.append(char)
        elif char == ')':
            while not ( charstack[-1] == '('):
                output = output + charstack[-1]
                charstack.pop()
            charstack.pop()
            
        else:
            while not precedence(char, charstack[-1]):
                output = output + charstack.pop()
            charstack.append(char)

    print(output)

postfix("((8*5+3)-7)-(5*3)") 

