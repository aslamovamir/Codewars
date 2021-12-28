# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should 
# be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(message):
    
    answer = ""
    for char in message:
        if char.isalpha():
            
            if char.isupper():
                if ord(char) + 13 > 90:
                    answer += chr((ord(char)+13)%90 + 64)
                elif ord(char) + 13 == 90:
                    answer += chr(90)
                else:
                    answer += chr((ord(char)+13)%90)
            else:
                if ord(char) + 13 > 122:
                    answer += chr((ord(char)+13)%122 + 96)
                elif ord(char) + 13 == 122:
                    answer += chr(122)
                else:
                    print((ord(char)+13)%122)
                    answer += chr((ord(char)+13)%122)
        else:
            answer += char

    return answer
