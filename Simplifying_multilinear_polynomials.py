# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy 
# ("2x+xy"). But tell that to your pc and we'll see! 

# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"),
# and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

# All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
# "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab" 


# All monomials appears in order of increasing number of variables, e.g.:
# "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz" 

# If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
# "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz" 

# There is no leading + sign if the first coefficient is positive, e.g.:
# "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

# N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something 
# like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

# Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

# Good Work :)

def simplify(poly):
    runner = ""
    MapCoef = {}
    digits = []
    sign = ''
    for i in range(0, len(poly)):
        if poly[i].isdigit():
            digits.append(poly[i])
            continue
        if poly[i] == '-' and i == 0:
            sign = '-'
            continue
        if poly[i] == '-' or poly[i] == '+' or i == len(poly)-1:
            if i == len(poly)-1:
                runner += poly[i]
            runner = ''.join(sorted(runner))
            digits.reverse()
            if digits == []:
                if sign == '+' or sign == '':
                    coefficient = 1
                else:
                    coefficient = -1
            else:
                coefficient = int(''.join(digits))
                if sign == '-':
                    coefficient = 0 - coefficient
            if runner not in MapCoef:
                MapCoef[runner] = coefficient
            else:
                MapCoef[runner] += coefficient
                    
            digits.clear()
            runner = ""
            sign = poly[i]
            continue
        runner += poly[i]
    
    
    for key, value in MapCoef.items():
        print(key, ": ", value)
    
    answer = ""
    # we will append the variables accoring to the number of letters they have
    # min-number letters variables go first
    # let's store all the variables in a seperate list
    variables = []
    
    for key, value in MapCoef.items():
        variables.append(key)

    # sort the list
    variables.sort()
    # list expression is a lis =t of expressions to be later sorted according to length
    list_expression = []
    min_var = variables[0]
    min = len(variables[0])
    while len(variables) != 0:
        for variable in variables:
            if min > len(variable):
                min = len(variable)
                min_var = variable
        if MapCoef[min_var] == 1:
            list_expression.append('+' + min_var)
        elif MapCoef[min_var] > 1:
            list_expression.append('+' + str(MapCoef[min_var]) + min_var)
        elif MapCoef[min_var] < -1:
            list_expression.append(str(MapCoef[min_var]) + min_var)
        elif MapCoef[min_var] == -1:
            list_expression.append('-' + min_var)

        variables.remove(min_var)
        if len(variables) != 0:
            min_var = variables[0]
            min = len(min_var)

    # copy the variables from the list into a string
    for variable in list_expression:
        answer += variable
    # if the first char is a '+', we know we don't need it
    if answer[0] == '+':
        answer = answer[1:]
    return answer
