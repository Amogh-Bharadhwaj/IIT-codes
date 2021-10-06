'''Accept a positive integer nn as input and print the identity matrix of size n \times nn×n. 
Your output should have nn lines, where each line is a sequence of nn comma-separated integers that corresponds to one row of the matrix.'''
n = int(input())
line = ''

for i in range(n):
    for j in range(n):
        if(i == j):
            line = line + '1'
        else:
            line = line + '0'
        if j < n-1:
            line = line + ','
    print(line)    
    line = ''