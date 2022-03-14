
'''
Consider a social network of friends/relatives, most of whom are closely connected.
Visualize this as a graph where each vertex denotes a person,
and if two people know each other there is an edge between the vertices denoting them.
If persons x and y know each other directly,
then there is an edge connecting x and y and level of connectivity between them is 1.
If person x is a friend of person y and person y is friend of person z,
but x is not a friend of z, then the level of connectivity between x and z is 2, and so on.
The connectivity between people is always two way,
i.e. if x directly knows y, then y also knows x directly.
Complete the Python function findconnectionLevel(n, Gmat, Px, Py) that takes 4 arguments,
number of persons n (n persons numbered from 0 to n-1),
Gmat an adjacency matrix representation of n persons and their connections
(if Gmat[x][y] = 1, then person x and y are directly connected),
two persons Px and Py both numbers, and returns the minimum level of connectivity between Px and Py.
Return 0 if px and Py are not connected through anybody in the group.
'''

def neighbours(AMat,i,n):
  nbrs = []
  (rows,cols) = n,n
  for j in range(cols):
    if AMat[i][j] == 1:
      nbrs.append(j)
  return nbrs


class Queue:
  def __init__(self):
    self.queue = []
  
  def addq(self,v):
    self.queue.append(v)
  
  def delq(self):
    v = None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
    return(v)
  
  def isempty(self):
    return(self.queue == [])
  
  def __str__(self):
    return(str(self.queue))

def BFS(AMat, v,n):
  (rows,cols) = n,n
  (visited, level) = ({},{})
  for i in range(rows):
    visited[i] = False
    level[i] = 0
  q = Queue()

  visited[v] = True
  q.addq(v)

  while(not q.isempty()):
    j = q.delq()
    for k in neighbours(AMat, j,n):
      if(not visited[k]):
        level[k] = level[j]+1
        visited[k] = True
        q.addq(k)
  return(visited, level)


def findConnectionLevel(n,Gmat,Px,Py):
    (v,l) = BFS(Gmat,Px,n)
    return l[Py]
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))
