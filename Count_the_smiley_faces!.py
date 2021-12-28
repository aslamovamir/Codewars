# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]
                        
# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

def count_smileys(arr):
    
    if not arr:
        return 0
    else:
        valid_eyes = [':', ';']
        valid_noses = ['-', '~']
        valid_mouths = [')', 'D']
        
        answer = 0
        for smile in arr:
            if smile[0] in valid_eyes:
                if len(smile) == 3:
                    if smile[1] in valid_noses:
                        if smile[2] in valid_mouths:
                            answer += 1
                elif len(smile) == 2:
                    if smile[1] in valid_mouths:
                        answer += 1
    
        return answer
