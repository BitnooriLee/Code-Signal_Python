'''Given two strings, find the number of common characters between them.'''


def commonCharacterCount(s1, s2):
    s11=list(s1)
    s12=list(s2)
    count=0
    for c in s11:
        if c in s12:
            count+=1
            s12.remove(c)

    return count
