'''Write a Python function combination Sort(strList) that takes a list of unique strings strlist as an argument, 
where each string is a combination of a letter from a to z and a number from 0 to 99, 
the initial character in string being the letter. 
For example a23, d5, 999 are some strings in this format. 
This function should sorts the list and return two lists (L1, L2) in the order mentioned below.
L1: First list should contain all strings sorted in ascending order with respect to the first character only. 
    All strings with same initial character should be in the same order as in the original list.
L2: In the list L1 above, sort the strings starting with same character, 
    in descending order with respect to the number formed by the remaining characters.''' 
def InsertionSort(L):
    n = len(L)
    for i in L:
        if n <= 1:
            return L
        for i in range(n):
            j = i
            while(j > 0 and int(L[j][1:]) > int(L[j-1][1:])):
                (L[j], L[j-1]) = (L[j-1], L[j])
                j = j-1
    return L   
def Sort(L):
    n = len(L)
    if n < 1:
        return L
    for i in range(n):
        j = i
        while(j > 0 and ord(L[j][0]) < ord(L[j-1][0])):
            (L[j], L[j-1]) = (L[j-1], L[j])
            j = j-1
    L1 = []
    i=0
    while i in range(len(L)-1):
        row = 1
        check = L[i][0]
        for j in range(i+1,len(L)):
            if L[j][0] == check:
                row += 1
        for j in InsertionSort(L[i:i+row]):
            L1.append(j)
        i += row
    return L,L1
print(Sort(['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']))