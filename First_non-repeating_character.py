# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    freq_map = {}
    print(string)
    
    runner = string.lower()
    # collect the frequencies of the chars
    for char in runner:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    # go through the string and return the first char with freq == 1
    for char in string:
        if freq_map[char.lower()] == 1:
            return char
    
    return ''
  
