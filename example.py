# Problem 1

A = [[4, 7, 2, 8],
     [6, 3, 5, 1],
     [9, 2, 6, 4],
     [3, 8, 1, 7]]

def analyze_matrix(matrix):
    max_val = float('-inf') 
    max_row = -1
    max_col = -1
    diagonal_sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            if element > max_val:
                max_val = element
                max_row = i
                max_col = j
        
        if i < len(matrix[i]): 
            diagonal_sum += matrix[i][i]

    return max_val, max_row, max_col, diagonal_sum

maximum_value, max_row_idx, max_col_idx, diagonal_sum_value = analyze_matrix(A)
print(f"The maximum value in matrix A is: {maximum_value} at position ({max_row_idx}, {max_col_idx})")
print(f"The sum of the diagonal elements in matrix A is: {diagonal_sum_value}")

# problem 2

def f(x):
    return x**3 - 2*x**2 + x

def derivative(x, h):
    return (f(x + h) - f(x)) / h

h_value = 0.001
x_values = [0, 1, 2, 3, 4]

print(f"Calculating derivative of f(x) = x^3 - 2x^2 + x at h = {h_value}:")
for x_val in x_values:
    deriv_at_x = derivative(x_val, h_value)
    print(f"Derivative at x = {x_val}: {deriv_at_x:.6f}")


#4
    A = [[1,2,3], [4,5,6]]
B = [[2,1],[3,2],[1,4]]

def matrix_multiply(matrix_a, matrix_b):
  
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    
    if cols_a != rows_b:
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b): 
            for k in range(cols_a): 
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix


C = matrix_multiply(A, B)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResult of A * B:")
for row in C:
    print(row)



#5

student_data = [
    {"id": 101, "name": "Alice", "score": 78, "grade": "B"},
    {"id": 102, "name": "Bob", "score": 35, "grade": "F"},
    {"id": 103, "name": "Rahul", "score": 85, "grade": "A"},
    {"id": 104, "name": "Priya", "score": 67, "grade": "B"},
    {"id": 105, "name": "John", "score": 42, "grade": "C"}
]

print("----- Student Results -----")
for student in student_data:
    print(f"{student['id']} {student['name']} {student['score']} {student['grade']}")

total_students = len(student_data)
print(f"Total students = {total_students}")    



    
