'''https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ#
Given the string, check if it is a palindrome.'''

def checkPalindrome(inputString):
    length=len(inputString)
    if length==1:
        return True

    else:
        for i in range(0, int(round(length/2))):
            if inputString[i]!=inputString[length-i-1]:
                return False
        return True
