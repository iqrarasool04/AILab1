def levDistance(str1, str2):
    # creating a 2d array
    matrix = [[0] * (len(str2) + 1) for row in range(len(str1) + 1)]
        
    #initializing array
    for row in range(len(str1)+1):
        matrix[row][0] = row
    for col in range(len(str2)+1):
        matrix[0][col] = col
    
    #finding distance
    for row in range(1,len(str1)+1):
        for col in range(1,len(str2)+1):
            if str1[row-1]==str2[col-1]:
                cost = 0
            else:
                cost = 1
            matrix[row][col] = min(matrix[row-1][col],
                                   matrix[row][col-1],
                                   matrix[row-1][col-1])+cost
    
    # printing array
    for i in matrix:
        for x in i:
            print(x,end=" ")
        print()

    return matrix

def calculateOperations(matrix,str1,str2):
    #calculating number of operations
    i = len(str1)
    j = len(str2)
    operations = {"deletions":0, "insertions":0, "substitutions":0}
    while i>0 and j>0:
        if (str1[i-1] == str2[j-1]):
            i-=1
            j-=1
        else:
            if (matrix[i][j] == matrix[i-1][j]+1):
                operations["deletions"]+=1
                i-=1
            elif (matrix[i][j] == matrix[i][j-1]+1):
                operations["insertions"]+=1
                j-=1
            else:
                operations["substitutions"]+=1
                i-=1
                j-=1
    
    return operations
    
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
levMatrix = levDistance(str1,str2)
distance = levMatrix[len(str1)][len(str2)]
print("Levenshtein/Edit distance between the two strings is ",distance)

operations = calculateOperations(levMatrix,str1,str2)
print("Number of deletions are ",operations["deletions"])
print("Number of insertions are ",operations["insertions"])
print("Number of substitutions are ",operations["substitutions"])
    
