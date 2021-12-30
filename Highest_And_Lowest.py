# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    int_list = []
    numbers = numbers.split(" ")
    for num in numbers:
        int_list.append(int(num))
    
    max_n = max(int_list)
    min_n = min(int_list)
    
    return f"{max_n} {min_n}"
