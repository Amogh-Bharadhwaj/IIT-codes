'''WAP that accepts a list L and a integer P where L>P.
The task is to pick P elements from the list L,
where the difference bw the max and min in the selected elements is minimum
compared to other differences in possible subset of p elements.
The function returns this min difference value.'''
def find_Min_Difference(L,P): 
    dif = 100000
    for i in L:
        newl = []
        n = []
        l = L[:]
        l.remove(i)
        for j in range(P):
            n = [abs(i-x) for x in l]
            newl.append(l[n.index(min(n))])
            l.remove(l[n.index(min(n))])
        print(newl)
        if max(newl) - min(newl) < dif:
            dif = max(newl) - min(newl)
    return dif
print(find_Min_Difference([1,2,3,-4,3,2,1,5,-6,7,8,9,10], 6))