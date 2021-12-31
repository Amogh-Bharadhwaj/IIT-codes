'''Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , 
that returns all unique twin primes between m and n (both inclusive). 
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.'''
def Twin_Primes(n,m):
    prime = []
    twin = []
    for i in range(n,m+1):
        flag = 0
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    for i in range(len(prime)-1):
        if prime[i] - prime[i+1] == -2:
            twin.append((prime[i],prime[i+1]))
    return tuple(twin)
print(Twin_Primes(int(input("Enter lower limit: ")), int(input("Enter upper limit: "))))