'''Write a function named is_magic that accepts a square matrix as argument and returns YES if it is a magic-square and NO if it isn't one.'''

def is_magic(mat) :
  n = len(mat)
  sumd1=0
  sumd2=0
  for i in range(n):
    sumd1+=mat[i][i]
    sumd2+=mat[i][n-i-1]
  if not(sumd1==sumd2):
    return 'NO'
  for i in range(n):
    sumrow=0
    sumcol=0
    for j in range(n):
      sumrow+=mat[i][j]
      sumcol+=mat[j][i]
    if not(sumrow==sumcol==sumd1):
      return 'NO'
  return 'YES'