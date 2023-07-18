def column_sums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    sums = [0] * cols

    for i in range(rows):
        for j in range(cols):
            sums[j] += matrix[i][j]

    return sums

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)

result = column_sums(matrix)
print(result)