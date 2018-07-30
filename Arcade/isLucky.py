'''Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.'''

def isLucky(n):
    value=[]
    count=0
    cmp=0
    while n>=1:
            value.append(n%10)
            n=n//10
            count+=1

    for i in range(int(count/2)):
        cmp+=value[i]
    if cmp*2==sum(value):
        return True
    else:
        return False
