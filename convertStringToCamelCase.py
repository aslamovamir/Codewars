# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output
# should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    camel_cased = ""
    found_dash = False
    for char in text:
        if found_dash:
            camel_cased += char.upper()
            found_dash = False
            continue
        if char == '-' or char == '_':
            found_dash = True
            continue
        camel_cased += char
    
    return camel_cased
