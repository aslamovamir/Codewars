# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with 
# the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    Stack = []
    for item in iterable:
        if item not in Stack:
            Stack.append(item)
        else:
            if Stack[len(Stack)-1] == item:
                continue
            else:
                Stack.append(item)
    
    return Stack
