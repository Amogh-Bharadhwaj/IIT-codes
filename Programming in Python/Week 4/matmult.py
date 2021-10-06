A=[]
n=int(input())         
for i in range(n): 
   A.append(input().split(','))
   
B=[]
for i in range(n): 
   B.append(input().split(','))
result=[[0 for i in range(n)] for i in range(n)]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result [i][j]+=int(A[i][k])*int(B[k][j])
for i in range(len(result)):
    print(*result[i], sep = ",") 

