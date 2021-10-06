'''A list L of words is already given to you as a part of the prefix code. Print the longest word in the list.
If there are multiple words with the same maximum length, print the one which appears at the rightmost end of the list.'''
L = input().split(',')
max = 0
word = ''
for i in range(len(L)):
    if len(L[i]) >= max:
        max = len(L[i])
        word = L[i]
print(word)