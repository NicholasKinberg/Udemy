# backtracking algorithm is problem-solving algorithm that uses brute force approach to find desired output
# brute force approach
    # backtracking
        # all solutions
    # dynamic programming
        # best solution (with space and time optimization)

# 3 types of problems in backtracking
    # decision problem: search for a feasible solution
    # optimization problem: search for the best solution
    # enumeration problem: find all feasible solutions

# 1. backtracking checks with a given node is a valid solution
# 2. discard invalid solutions with one iteration
# 3. enumerate all subtree of node to find valid solution

# Queens Problem
# Problem statement: Place N queens on an NxN chess board, in such a manner that no two queens can attack each other
    # For example, 4 queens on a 4x4 chess board
    # Not same column, not same row, not same diagonal so no two queens can attack each other

# Pseudocode:
    # 1. Start in leftmost column (index[i][0])
    # 2. If all queens are placed
        # 2a. return true
    # 3. Try all rows in current column(index[i][j])
        # 3a. For every row, if queen can be placed safely in this row, then mark this [row, column] as part of solution and recursively check if placing queen here leads to solution
        # 3b. If placing queen in [row, column] leads to solution, return true
        # 3c. If placing queen doesn't lead to solution then unmark this [row, column], (backtrack) and go to step (a) to try other rows
    # 4. If all rows have been tried and nothing worked, return false to trigger backtracking

class NQueens:
    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]
    
    def print_queens(self):
        for i in range(self.n): # rows
            for j in range(self.n): # columns
                if self.chess_table[i][j] == 1:
                    print(" Q ", end='') # for every cell we assign to 1, we place a queen there
                else:
                    print(" - ", end='') # otherwise we print nothing
            print("\n") # return function in print statement
    
    def is_place_safe(self, row_index, col_index):
        # checks horizontally
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False # returns False whenever we encounter a row that has a queen
        # top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1): # range(row_index, -1, -1) to check diagonally
            if i < 0:
                break # terminates the program because it is impossible for there to be negative rows
            if self.chess_table[i][j] == 1:
                return False # returns False whenever we land on a place with a queen
            j = j - 1 # column iterates back one by one
        return True
    
    def solve(self, col_index):
        if col_index == self.n: # checking that number of columns input by user is same number of columns input at time of initiation of chess board
            return True
        for row_index in range(self.n):
            if self.is_place_safe(row_index, col_index):
                self.chess_table[row_index][col_index] = 1 # assign a 1 to every cell that is safe from queens
            if self.solve(col_index+1): # backtracking algorithm, for every place that is NOT safe because otherwise the if statement would use the two lines above instead of this one
                return True
            self.chess_table[row_index][col_index] = 0 # else chess_table just equals 0
        return False # return False as a fail-safe in case there is no safe spot