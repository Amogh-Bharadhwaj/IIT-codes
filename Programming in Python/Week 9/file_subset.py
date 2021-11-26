'''Write a function named relation that accepts these two text files as arguments. It should return the string Subset if file1 is a subset of file2.
It should return Equal if file1 is equal to file2. If both these conditions are not satisfied, it should return the string No Relation.'''

def relation(file1,file2):
    f = open(file1,'r')
    g = open(file2,'r')
    l = f.readlines()
    m = g.readlines()
    count = 0
    for i in range(len(l)):
        l[i]=l[i].strip()
        m[i]=m[i].strip()
        if l[i] == m[i]:
            count += 1
    if l == m:
        return 'Equal'
    elif count == len(l):
        return "Subset"
    return 'No Relation'
