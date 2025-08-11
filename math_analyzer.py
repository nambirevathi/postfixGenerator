

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

    print(f"called obtainindicies for {math_equation} returning  and {left_ind} and {right_ind} ")
    return  left_ind, right_ind

def get_num_to_str(num_str):

    num_to_str_map = {}
    num_to_str_map['1'] = 'one'
    num_to_str_map['2'] = 'two'
    num_to_str_map['3'] = 'three'
    num_to_str_map['4'] = 'four'
    num_to_str_map['5'] = 'five'
    num_to_str_map['6'] = 'six'
    num_to_str_map['7'] = 'seven'
    num_to_str_map['8'] = 'eight'
    num_to_str_map['9'] = 'nine'
    num_to_str_map['0'] = 'zero'


    verbal_num = ''

    for char in num_str:
        verbal_num = verbal_num + num_to_str_map[char]

    return verbal_num


def math_to_postfix(operators, math_equation, symbol_dict):
    '''
    Given a bedmas expression convert it into postfix
    '''
    #baseline check

    print(f"entered math_to_postfix with  {math_equation} using dict {symbol_dict}")

    if(')' in math_equation):
        while(')'  in math_equation):
            i, j = obtain_indicies(math_equation)
            math_symbol, symbol_dict = math_to_postfix(operators, math_equation[i+1:j], symbol_dict)
            print(f"obtained math symbol of {math_symbol} for eq {math_equation[i:j+1]} ")
            if(str(math_symbol) not in symbol_dict):
                symbol_dict[str(math_symbol)] = "symbol_" +  get_num_to_str(str(len(symbol_dict)))
            new_math_equ = math_equation[:i] + symbol_dict[str(math_symbol)] + math_equation[j+1:] 
            print(f"new math eq is {new_math_equ}")
            math_equation = new_math_equ

    baseline = True

    for op in operators:
        if(op in math_equation):
            baseline = False

    if(baseline and (math_equation in symbol_dict.values())):
        return [math_equation], symbol_dict  
    
    numerics = [str(i) for i in range(0, 10)]
    if(baseline):
        num_str = ''
        for num in math_equation:
            if(num in numerics):
                num_str = num_str + num

        return [str(num_str)], symbol_dict


    for op in operators:

        for i  in range(len(math_equation)-1, -1, -1):
            char = math_equation[i]

            if(op==char):
                left_value, symbol_dict = math_to_postfix(operators, math_equation[:i], symbol_dict)
                right_value, symbol_dict = math_to_postfix(operators, math_equation[i+1:], symbol_dict)
                return left_value + right_value + [op], symbol_dict


if(__name__=="__main__"):
    operators = ['^', '/', '*', '+', '-']
    operators.reverse()
    print("operator used are ", operators)
    temp_dict = {}
    x, symbol_dict = math_to_postfix(operators, '(2+3)*4 - 5', temp_dict)

    ans = []

    revs_st = {}

    for key, val in symbol_dict.items():
        revs_st[val] = key

    for val in x:
        if(val in symbol_dict.values()):
            ans.append(revs_st[val])
        else:
            ans.append(val)
    print(x)
    print(ans)
