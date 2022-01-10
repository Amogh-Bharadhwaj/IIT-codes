'''Consider a list L containing n integers, 
where each integer i is in the range [0, r) that is 0 <= i<r, r<1000 and n>>r(n is much greater than r). 
Write a Python function sortInRange (L, r) to sort the list L in ascending order. 
Try to write a solution that runs in O(n+r) asymptotic complexity.'''

def sortInRange(L,r):
  n = len(L)
  if n < 1:
    return L
  for i in range(n):
    j = i
    while(j > 0 and L[j] < L[j-1]):
      (L[j], L[j-1]) = (L[j-1], L[j])
      j = j-1
  return L
print(sortInRange([2,0,1,1,2,3,0,2,1,0,2,3,1,2],4))