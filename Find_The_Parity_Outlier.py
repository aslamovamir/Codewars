# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is
# either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a 
# method that takes the array as an argument and returns this "outlier" N.

# Examples

# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):

    found_even = False
    found_odd = False
    even_array = False
    odd_array = False
    
    for num in integers:
        if num%2 == 0:
            if not found_even:
                found_even = True
                even = num
            else:
                even_array = True
        elif num%2 != 0:
            if not found_odd:
                found_odd = True
                odd = num
            else:
                odd_array = True
    
    if even_array:
        return odd
    else:
        return even
