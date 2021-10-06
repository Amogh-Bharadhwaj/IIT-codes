'''You are given a list marks that has the marks scored by a class of students in a Mathematics test. 
Find the median marks and store it in a float variable named median. 
You can assume that marks is a list of float values.'''
marks = [60,10,30,40,20,50]
score = []
mini = marks[0]
index = -1
for i in range(len(marks)):
    for j in range(len(marks)):
        if marks[j] < mini:
            mini = marks[j]
    score.append(mini)
    marks.remove(mini)
    mini = 999999
if len(score)%2 == 1:
    median = score[(len(score)//2)]
else:
    median = (score[(len(score)//2)-1] + score[(len(score)//2)])/2
print(median)