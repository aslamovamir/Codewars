# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

# Sudoku rules:

# Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

# Rows:


# There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers 
# in any row. In other words, there can not be any rows that are identical.

# In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in
# to complete the row.

# Columns:


# There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 
# 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

# In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the 
# column.

# Regions


# A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

# Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not 
# permitted in any region. Each region will differ from the other regions.

# In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the 
# region.

def done_or_not(board): #board[i][j]
    
    for arr in board:
        print(arr)
    Set = set()
    
    # let's first check the rows
    for row in board:
        for num in row:
            if num not in Set:
                Set.add(num)
            else:
                return 'Try again!'
        Set.clear()
        
    # let's check the columns
    for i in range(0, 9):
        for j in range(0, 9):
            if board[j][i] not in Set:
                Set.add(board[j][i])
            else:
                return 'Try again!'
        Set.clear()
    
    # let's check the regions 3X3
    row = 0
    col = 0
    row_state = 0
    col_state = 0
    
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                for l in range(0, 3):
                    print(board[row][col])
                    if board[row][col] not in Set:
                        Set.add(board[row][col])
                    else:
                        return 'Try again!'
                    col += 1
                row += 1
                col = col_state
            Set.clear()
            row_state += 3
            row = row_state
            col = col_state
        col_state += 3
        col = col_state
        row_state = 0
        row = row_state
        
    return 'Finished!'
  
