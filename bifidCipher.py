def input_matrix(rows, cols):
    values = "B G W K Z Q P N D S I O A X E F C L U M T H Y V R".split()
    # Ensure correct number of values
    if len(values) != rows * cols:
        print("Error: The number of values entered does not match the matrix size.")
        return None
    # Fill matrix with the values
    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(values[index])
            index += 1
        matrix.append(row)
    
    return matrix

def letter_indexes(matrix, letter):
    indexes = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == letter:
                indexes.append((i, j))
    return indexes
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
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == letter:
                indexes.append((i, j))
    return indexes

message = "This is a message"

row_indices = []
col_indices = []

for char in message:
    char = char.upper()  # Convert to uppercase to match matrix values
    if char != ' ':  # Skip spaces
        indexes = letter_indexes(square, char)
        if indexes:
            for row, col in indexes:
                row_indices.append(row + 1)  # Adding 1 to index to start from 1 instead of 0
                col_indices.append(col + 1)  # Adding 1 to index to start from 1 instead of 0
        else:
            print(f"'{char}' not found in the matrix.")

# Print all row and column indices in the desired format
if row_indices and col_indices:
    print(f"{', '.join(map(str, row_indices))}")
    print(f"{', '.join(map(str, col_indices))}")

combined = row_indices + col_indices
print(combined)

def get_characters_from_indices(matrix, indices):
    characters = []
    for i in range(0, len(indices), 2):  
        row = indices[i] - 1  
        col = indices[i + 1] - 1  
        characters.append(matrix[row][col])
    return characters

# Use the combined list of indices to get the characters
result_characters = get_characters_from_indices(square, combined)

# Print the characters as a string
print("".join(result_characters))
#combined_indices = [(row - 1, col - 1) for row, col in zip(row_indices, col_indices)]


#new_letter = square[row_index][col_index]

#print(row_indices[0,1])

#square = input_matrix(rows, cols)
#print(square)

#row_index = 4
#col_index = 1
#newChar = square[row_index][col_index]
#print(row_index, col_index)
#list out rows
#list out columns
#for char in indexes:
 #   print(char[0])