# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines
# whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    # convert the input to lowercase
    string = string.lower()
    # collect all the chars in a Set
    Set = set()
    for char in string:
        if char in Set:
            return False
        else:
            Set.add(char)
    
    return True
