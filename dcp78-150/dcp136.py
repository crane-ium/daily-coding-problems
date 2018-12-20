#A binary N x M matrix
#Find the largest rectangular subset that only contains 1's

#Give a 2d list
def get_largest_rectangle(matrix):
    #Let's categorize the matrix by counting horizontal and vertical connections, seperately
    #ie. 1, 1, 1    1, 2, 3     1, 1, 1             1, 2, 3
    #    0, 1, 1 -> 0, 1, 2  &  0, 2, 2 multiply -> 0, 2, 4
    #    1, 1, 0    1, 2, 0     1, 3, 0             1, 6, 0
    #
    #This means we can create a priority queue to check where the largest rectangle could be
    #1. If we multiply the matrices we can find the max possible rectangle size quantified
    #   by the bottom right corner of it. In our example, the max possible is at (2, 1): 6
    #2. Verify each possible largest by checking the max in the heap, and if the adjacent
    #   columns to the left or the adjacent rows upward are >= the cell at (i, j)
    row_adj_matrix = gen_row_matrix(matrix)
    col_adj_matrix = gen_col_matrix(matrix)
    # mult_matrix = []
    #Multiply corresponding indeces in each matrix, and push them into a list we can sort based on their multiplication
    #   Then, we must verify through the sorted list (priority queue)
    priority_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[-1])):
            priority_list.append((row_adj_matrix[i][j] * col_adj_matrix[i][j], i, j)) #Throw in tuples
    #Sort tuples in p-list
    priority_list.sort(key=lambda x:x[0], reverse=True)
    #Now we have a list of highest potential areas, let's verify each one until we find a valid bottom right.
    #If it's verified, then we know it's the greatest possible
    #This approach will use more space but it uses less time, which I believe is more important
    for tup in priority_list:
        valid = True
        height = col_adj_matrix[tup[1]][tup[2]] #Rows
        width = row_adj_matrix[tup[1]][tup[2]] #Cols
        #Check vertical
        for i in range(1, height):
            valid &= row_adj_matrix[tup[1]-i][tup[2]] >= height
        for j in range(1, width):
            valid &= col_adj_matrix[tup[1]][tup[2]-j] >= width
        if valid:
            print(f'{tup[1:]} is bot-right corner of rectangle with area {tup[0]}')
            return tup[0]

def gen_row_matrix(matrix):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_row = []
        for j in range(len(row)):
            new_cell = ((new_row[-1] if new_row else 0) + 1) * matrix[i][j]
            new_row.append(new_cell)
        new_matrix.append(new_row)
    return new_matrix

def gen_col_matrix(matrix):
    new_matrix = [[] for _ in range(len(matrix))]
    for j in range(len(matrix[-1])):
        for i in range(len(matrix)):
            new_cell = ((new_matrix[i-1][j] if i > 0 else 0) + 1) * matrix[i][j]
            new_matrix[i].append(new_cell)
    return new_matrix

def mult_matrices(matrix1, matrix2):
    #We must assume matrices are identical size
    new_matrix = [[] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            new_matrix[i].append(matrix1[i][j] * matrix2[i][j])
    return new_matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 1, 1], [1, 1, 0], [0, 0, 0]]
    matrix2 = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
    new_matrix = gen_row_matrix(matrix)
    col_matrix = gen_col_matrix(matrix)
    # print(new_matrix)
    # print(col_matrix)
    # print(mult_matrices(new_matrix, col_matrix))
    print(get_largest_rectangle(matrix))
    print(get_largest_rectangle(matrix2))
    # Ultimately, my space is worse than the given solution, but the time complexity is superior
    