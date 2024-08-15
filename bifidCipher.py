def input_matrix(rows, cols):
    #values = input(f"Enter {rows * cols} values, separated by spaces: ").split()
    values = "B G W K Z Q P N D S I O A X E F C L U M T H Y V R".split()
    # Ensure we have the correct number of values
    if len(values) != rows * cols:
        print("Error: The number of values entered does not match the matrix size.")
        return None
    
    # Fill the matrix with the entered values
    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(values[index])
            index += 1
        matrix.append(row)
    
    return matrix

# Define matrix dimensions
rows = 5
cols = 5

# Get matrix input
square = input_matrix(rows, cols)

# Print the matrix
if square:
    for row in square:
        print(row)
        
def letterIndexes(matrix, letter):
    indexes = []
    