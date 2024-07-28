def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result_1 = get_matrix(n=4, m=2, value=12)
result_2 = get_matrix(n=5, m=9, value=4)
result_3 = get_matrix(n=8, m=7, value=6)

print(result_1)
print(result_2)
print(result_3)