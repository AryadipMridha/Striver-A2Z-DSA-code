from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Access any col [0][..] and any row by [..][0]
        # traverse the matrix
        col0 = False  # Initialize flag to track if the first column needs to be zeroed out
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        size_row = len(matrix)  # Number of rows in the matrix
        size_col = len(matrix[0])  # Number of columns in the matrix
        for i in range(size_row):  # Loop through each row
            for j in range(size_col):  # Loop through each column
                if matrix[i][j] == 0:  # If current element is zero
                    # mark the ith row
                    matrix[i][0] = 0  # Mark the corresponding row entry as zero

                    # mark jth col
                    if j != 0:  # If current column is not the first column
                        matrix[0][j] = 0  # Mark the corresponding column entry as zero
                    else:  # If current column is the first column
                        col0 = True  # Set flag indicating first column needs to be zeroed
        # Leaving the first row and first col untouched, Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1, size_row):  # Loop through rows starting from the second row
            for j in range(1, size_col):  # Loop through columns starting from the second column
                if matrix[i][0] == 0 or matrix[0][j] == 0:  # If corresponding row or column entry is zero
                    matrix[i][j] = 0  # Mark the current element as zero
        # step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:  # If the first element is zero
            for j in range(size_col):  # Loop through each column
                matrix[0][j] = 0  # Mark the first row as zero

        if col0:  # If flag indicates first column needs to be zeroed
            for i in range(size_row):  # Loop through each row
                matrix[i][0] = 0  # Mark the first column as zero

        return matrix  # Return the modified matrix
