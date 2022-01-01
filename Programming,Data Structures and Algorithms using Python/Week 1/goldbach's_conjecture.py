'''Write a function Goldback(n) where n is a +ve number >2 that returns a list
of tuples. In each tulpe(a,b) where a<=b, a and b should be prime numbers and
the sum of a and b should add upto n'''
def Goldbach(n):
    prime = []
    tuplist = []
    for i in range(2,n+1):
        flag = 0
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    for i in prime:
        for j in prime:
            if i+j == n:
                if (j,i) not in tuplist:
                    tuplist.append((i,j))
    return tuplist
n=int(input("Enter a number: "))
print(sorted(Goldbach(n)))