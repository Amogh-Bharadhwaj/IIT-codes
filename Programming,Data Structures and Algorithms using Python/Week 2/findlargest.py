def findLargest(l):
    start = 0
    end = len(l)-1
    if (end == start):
        return l[start]
    mid = start + (end - start) // 2
    if(mid==0 and l[mid]>l[mid+1]):
          return l[mid]
    if (mid < end and l[mid + 1] < l[mid] and mid>0 and l[mid]>l[mid-1]):
        return l[mid]
    if (l[start] > l[mid]):
        return findLargest(l[start:mid])
    else:
        return findLargest(l[mid+1:end+1])
print(findLargest([2,4,5,7,9]))