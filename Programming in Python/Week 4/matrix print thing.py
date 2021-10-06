'''Accept a square matrix as input and store it in a variable named matrix. 
The first line of input will be, nn, the number of rows in the matrix. Each of the next nn lines will have a sequence of nn space-separated integers.'''
n = int(input())
matrix = []
for i in range(n):
	line = input().split(' ')
	for j in range(len(line)):
		line[j] = int(line[j])
	matrix.append(line)
print(matrix)