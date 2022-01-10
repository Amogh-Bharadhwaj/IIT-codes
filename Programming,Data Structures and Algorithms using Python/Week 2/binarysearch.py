'''Write a Python function binarySearchIndexAnd Comparisons(L, k) that accepts a list L sorted in ascending order 
and an integer k and returns a tuple (True/False, numComparisons). 
The first part of this tuple will be True if integer k is present in list L, False otherwise. 
The second part of the tuple is an integer which gives the number of elements in L 
that are actually compared to k while searching k in the list L using binary search.
For consistency use (left+right)//2 to calculate the middle index.'''

def binarySearchIndexAndComparisions(L,k):
    start = 0
    end = len(L) - 1
    count = 0
    mid = (start + end)//2
    while start <= end and mid in range(len(L)):
        mid = (start + end)//2
        if L[mid] == k:
            count += 1
            return True,count
        elif L[mid] > k:
            end = mid-1
            count +=1
        else:
            start = mid+1
            count += 1
    return False,count
print(binarySearchIndexAndComparisions([2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65], 11))