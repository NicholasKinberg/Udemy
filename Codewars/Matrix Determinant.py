# Problem statement: Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
################################################
import numpy as np

def determinant(a):
    return round(np.linalg.det(np.matrix(a))) # this is a bad solution because anyone can call an already-built package; the problem asks us to build our own determinant function
################################################
def determinant(matrix):
    #your code here
    result = 0
    l = len(matrix)

    #base case when length of matrix is 1
    if l == 1:
        return matrix[0][0]

    #base case when length of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #for length of matrix > 2
    for j in range(0, l):
        # create a sub matrix to find the determinant
        if l!=2:
            sub_matrix = []               
            sub_matrix = [(row[0:j]+row[j+1:]) for row in matrix[1:]] # matrix[1:] to isolate sub-matrices from overarching matrix
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix) # would need to use recursion for NxN matrices of increasing size
    return result
####
# to build the above function with recursion, I would start with the following logic
# result = result + (-1)**j * matrix[0][j] * determinant(sub_matrx)
    # I would use the above line to (1) initialize a cofactor, (2) multiply by the sub-matrix, (3) obtain the determinant of the sub_matrix through recursion, and (4) add the product of the first three items to the previous result
    # I would then initialize sub_matrix above line 31 here to add the rows together of row[0:j] and row[j+1:] for rows starting with second row (matrix[1:]) because Python indexes starting with 0
################################################
def determinant(m):
    ans,sizeM = 0, len(m)
    if sizeM == 1: return m[0][0]
    for n in range(sizeM):
        ans+= (-1)**n * m[0][n] * determinant([ m[i][:n]+m[i][n+1:] for i in range(1,sizeM) ]) # NEED RECURSION FOR THIS FUNCTION; this is a perfect case of solving a larger problem by solving repeating sub-problems
    return ans
################################################
def sub_determinant(matrix, i):
    sub_matrix = []
    for j in range(1,len(matrix)):
        sub_matrix.append(matrix[j][:i] + matrix[j][i+1:])
    return sub_matrix
    
def determinant(matrix):
    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        sum = 0
        for i in range(0,len(matrix)):
            if 1 == i & 1:
                sum = sum - matrix[0][i] * determinant(sub_determinant(matrix,i))
            else:
                sum = sum + matrix[0][i] * determinant(sub_determinant(matrix,i))
        return sum
################################################
import copy

def create_lesser_matrix(matrix, j):
    matrix_copy = copy.deepcopy(matrix)
    del matrix_copy[0]
    
    
    for row in matrix_copy:
        del row[j]
    return matrix_copy
    
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    for i in range(len(matrix)):
        det += (-1)**i * matrix[0][i] * determinant(create_lesser_matrix(matrix, i))
    return det
################################################
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    sign = 1
    for i in range(len(matrix[0])):
        det += sign*matrix[0][i]*determinant([line[:i]+line[i+1:] for line in matrix[1:]])
        sign *= -1
    return det
################################################
def minor(matrix, c):
    return [r[:c] + r[c + 1:] for r in matrix[1:]]

def determinant(matrix):
        return sum([(pow(-1, c)) * a * determinant(minor(matrix, c)) for c, a in enumerate(matrix[0])]) if len(matrix) > 1 else matrix[0][0]
################################################
def determinant(matrix):
    det = 0
    l=len(matrix)
    if(l==1):
        return matrix[0][0]
    for i in range(l):
        minor = [matrix[r][1:l] for r in range(l) if r!=i]
        det+=(1-i%2*2)*matrix[i][0]*determinant(minor)
    return det