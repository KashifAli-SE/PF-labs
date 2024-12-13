def multiply_matrices(matrix1, matrix2):
    size = len(matrix1)
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]
result_matrix = multiply_matrices(matrix1, matrix2)

# Print the result
print("Resultant matrix after multiplication:")
for row in result_matrix:
    print(row)
