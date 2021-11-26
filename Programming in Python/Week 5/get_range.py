'''Write a function named get_range that accepts a non-empty list of real numbers as argument.
It should return the range of the list.'''

def maxi(L):
    ma = L[0]
    for i in range(len(L)):
        if L[i] > ma:
            ma = L[i]
    return ma
def mini(L):
    mi = L[0]
    for i in range(len(L)):
        if L[i] < mi:
            mi = L[i]
    return mi
def get_range(L):
    return maxi(L) - mini(L)