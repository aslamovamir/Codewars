# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    # let's collect odd numbers in a seperate list
    odd = []
    for num in source_array:
        if num%2 != 0:
            odd.append(num)
    
    # now we sort this array
    odd.sort()
    
    # now we go through the array again
    # if we meet an odd number, we take a num from
    # the sorted odd list
    answer = []
    for num in source_array:
        if num%2 != 0:
            answer.append(odd.pop(0))
        else:
            answer.append(num)
    
    return answer
