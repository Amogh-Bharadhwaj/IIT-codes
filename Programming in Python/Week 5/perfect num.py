'''Write a function named is_perfect that accepts a positive integer n as argument and returns True if it is a perfect number, and False otherwise.'''

def is_perfect(n):
    summ = 0
    for i in range(1,n):
        if n%i == 0:
            summ += i
    if summ == n:
        return True
    return False
print(is_perfect(int(input())))