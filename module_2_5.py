def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = 4
m = 5
value = 12
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Неверное значение строк')
elif m <=0:
    print('Неверное значение столбцов')
# else:          2
#     for i in matrix:
#         print(*i)