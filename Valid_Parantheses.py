# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should 
# return true if the string is valid, and false if it's invalid.

# Examples

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parentheses(string):
    stack = []
    print(string)
    for brace in string:
        if brace == '(' or brace == ')':
            if brace == '(':
                stack.append(brace)
            else:
                if stack:
                    if stack.pop() == '(':
                        continue
                    else:
                        return False
                else:
                    return False

    if stack:
        return False
    else:
        return True
