n = int(input())
line = []
matrix = []
for i in range(n):
    for j in range(n):
        line.append(input())
    matrix.append(line)
    line = []
print(matrix)