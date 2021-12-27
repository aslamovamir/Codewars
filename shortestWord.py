# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    # split the string input into an array of words
    array = s.split(' ')
    shortest = len(array[0])
    for word in array:
        if len(word) < shortest:
            shortest = len(word)
    return shortest 
