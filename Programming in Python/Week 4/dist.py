'''You are given a sequence of nn points, (x_i,y_i), 1 <= i <= n, in the 2-D plane as input. Also, you are given a point PP with coordinates (x,y)(x,y). 
Print all points in the sequence that are nearest to PP. 
 If multiple points have the same least distance from PP, print the points in the order of their appearance in the sequence.'''
length = int(input())
points = []
for i in range(length):
    x = input().split(',')
    points.append(x)
find = input().split(',')
index = []
mini = 101
for i in range(length):
    dist = ((int(find[0])-int(points[i][0]))**2 + (int(find[1])-int(points[i][1]))**2)**1/2
    if dist <= mini:
        mini = dist
for i in range(length):
    dist = ((int(find[0])-int(points[i][0]))**2 + (int(find[1])-int(points[i][1]))**2)**1/2
    if dist == mini:
        index.append(points[i])
for i in range(len(index)):
  print(','.join('{}'.format(x) for x in index[i]))
