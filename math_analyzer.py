

def obtain_indicies(math_equation):

    left_brackets = []
    right_brackets = []
    right_ind = -2 
    left_ind = -2
    for i in range(len(math_equation)-1, -1, -1):
        char = math_equation[i]
        if(char==')'):
            if(len(right_brackets)==0):
                right_brackets.append(')') 
                right_ind = i
            
        if(char=='('):
            left_brackets.append('(')
            if(len(left_brackets)==len(right_brackets)):
                left_ind = i
                break

    return right_ind, left_ind

    

def math_to_postfix(operators, math_equation, symbol_dict):
    '''
    Given a bedmas expression convert it into postfix
    '''
    #baseline check


    if(')' in math_equation):
        while(')' not in math_equation):
            i, j = obtain_indicies(math_equation)
            math_symbol = math_to_postfix(math_equation[i:j+1], symbol_dict)
            if(math_symbol not in symbol_dict):
                symbol_dict[math_symbol] = "symbol_" + str(len(symbol_dict))
            new_math_equ = math_equation[:i] + math_symbol + math_equation[j+1:] 
            math_equation = new_math_equ

    baseline = True

    for op in operators:
        if(op in math_equation):
            baseline = False

    numerics = [str(i) for i in range(0, 10)]
    if(baseline):
        num_str = ''
        for num in math_equation:
            if(num in numerics):
                num_str = num_str + num

        return [str(num_str)]


    for op in operators:

        for i  in range(len(math_equation)-1, -1, -1):
            char = math_equation[i]

            if(op==char):
                left_value = math_to_postfix(operators, math_equation[:i])
                right_value = math_to_postfix(operators, math_equation[i+1:])
                return left_value + right_value + [op]


if(__name__=="__main__"):
    operators = ['^', '/', '*', '+', '-']
    operators.reverse()
    print("operator used are ", operators)
    x = math_to_postfix(operators, '(2+3)*4 - 5')
    print(x)

