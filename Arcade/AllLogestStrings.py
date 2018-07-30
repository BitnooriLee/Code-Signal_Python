'''Given an array of strings, return another array containing all of its longest strings.'''

def allLongestStrings(inputArray):
    result=[]
    maxlen=max(len(inputArray[i]) for i in range(len(inputArray)))
    for i in range(len(inputArray)):
        if maxlen==len(inputArray[i]):
            result.append(inputArray[i])
    return(result)
