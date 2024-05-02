# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
        return total