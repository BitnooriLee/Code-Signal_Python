'''After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

Help the bots calculate the total price of all the rooms that are suitable for them.'''

def matrixElementsSum(matrix):
    totalsum=0
    save=list(matrix)
    for i in range(len(save)-1):
        for j in range(len(save[0])):
            if matrix[i][j]==0:
                matrix[i+1][j]=0
        totalsum+=sum(matrix[i+1])
    return totalsum+sum(matrix[0])
