# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the 
# line should also be stripped out.
# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def solution(string,markers):
    
    answer = ""
    split = string.split('\n')
    for sentence in split:
        for char in sentence:
            if char in markers:
                break
            answer += char
        if sentence != split[len(split)-1]:
            answer += '\n'
    
    filtered = ""
    for i in range(0, len(answer)):
        if i+1 < len(answer) and answer[i+1] == '\n' and answer[i] == ' ' or i == len(answer)-1 and answer[i] == ' ': 
            continue
        filtered += answer[i]
        
    return filtered

