# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil

def next_bigger(n):
    # let's create a helper function to check if two numbers have 
    # the same digits
    def same_digits(n, k):
        # let's put all the present digits in n in a list
        digits_n = []
        while True:
            # get the last digit
            digit = n%10
            # update n
            n //= 10
            # store the digit in the list
            digits_n.append(digit)
            # check if n is a one digit-number now
            if n//10 == 0:
                # take that number and put in the list
                digits_n.append(n)
                break

        
        # now let's go through the digits of k and determine if all the 
        # digits are in the list
        # to ensure that the number of the same digits is the same in the two numbers
        # we will keep removing the found digit from the list
        while True:
            digit = k%10
            # check if the digit is in the list
            if digit not in digits_n:
                return False
            digits_n.remove(digit)
            k //= 10
            if k//10 == 0:
                if k not in digits_n:
                    return False
                else:
                    break
        
        return True
    
    # while the number does not have the same digits as n, we keep incrementing the
    # variable iterator
    iterator = n + 1
    while not same_digits(n, iterator):
        iterator += 1
    
    return iterator
